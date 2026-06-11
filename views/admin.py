from flask import Blueprint, render_template, redirect, url_for, flash, request, send_from_directory, current_app
from flask_login import login_required, current_user
from models.user import UserDB
from models.plans import PlanDB
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, BooleanField, IntegerField, FloatField
from wtforms.validators import DataRequired, Optional, Email, NumberRange
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .auth import role_required
from controllers.contact import ContactController
from models.superadmin_audit import SuperadminAuditDB
import os
import secrets
from datetime import datetime, timedelta
import pytz
from utils.utils import Config, load_payload
import sqlite3
admin_bp = Blueprint('admin', __name__)
limiter = Limiter(key_func=get_remote_address)
token = secrets.token_urlsafe(32)
config = Config(load_payload())
class UserEditForm(FlaskForm):
    """Form for editing user details.

    Intentionally does NOT carry these fields:

    * ``confirmation_token`` — rotated by the resend-confirmation
      endpoint, never hand-edited. A static token cannot expire and
      would either lock the user out or be reused forever.
    * ``phone_verification_code`` — same reason; the column stores
      a hash, not the cleartext code, so a superadmin UI input is
      meaningless.
    * KEM/SRP blob columns (srp_salt, srp_verifier, public_key,
      encrypted_private_key, kdf_salt) — the server has no UI to
      rewrite them. Modifying any of them would silently brick the
      user's login.

    ``password`` is also absent: the server is zero-knowledge, so a
    "change password" UI lives in the user's own profile, not here.
    """
    username = StringField('Username', validators=[DataRequired()])
    role = SelectField('Role', choices=[('free', 'Free'), ('bronze', 'Bronze'), ('silver', 'Silver'), ('gold', 'Gold'), ('admin', 'Admin'), ('superadmin', 'Superadmin')], validators=[DataRequired()])
    email = StringField('Email', validators=[Optional(), Email()])
    phone = StringField('Phone', validators=[Optional()])
    first_name = StringField('First Name', validators=[Optional()])
    last_name = StringField('Last Name', validators=[Optional()])
    storage_quota = IntegerField('Storage Quota (MB)', validators=[DataRequired(), NumberRange(min=0)])
    subscription_status = SelectField('Subscription Status', choices=[('active', 'Active'), ('inactive', 'Inactive')], validators=[DataRequired()])
    email_verified = BooleanField('Email Verified')
    phone_verified = BooleanField('Phone Verified')
    trial_start = StringField('Trial Start (YYYY-MM-DD)', validators=[Optional()])
    trial_end = StringField('Trial End (YYYY-MM-DD)', validators=[Optional()])
    submit = SubmitField('Update User')

class PlanForm(FlaskForm):
    """Form for creating or editing a subscription plan."""
    name = StringField('Plan Name', validators=[DataRequired()])
    storage_quota = IntegerField('Storage Quota (MB)', validators=[DataRequired(), NumberRange(min=0)])
    trial_days = IntegerField('Trial Days', validators=[DataRequired(), NumberRange(min=0)])
    price = FloatField('Price ($)', validators=[DataRequired(), NumberRange(min=0.0)])
    submit = SubmitField('Save Plan')

@admin_bp.route(f'/admin{token}', methods=['GET'])
@login_required
@role_required('admin', 'superadmin')
@limiter.limit("10 per minute")
def admin():
    """Plan catalog read view.

    Plan CRUD lives at ``/admin<token>/plans`` and
    ``/admin<token>/plans/edit/<name>`` so a single page is not also
    a destructive form. This view is now strictly a list of
    available plans, with a per-row edit link.

    User identity (list, edit, suspend, MFA reset, confirmation
    rotation) is the superadmin panel's job and lives at
    ``/superadmin<token>``.
    """
    plan_db = PlanDB(config.SQLALCHEMY_DATABASE_PATH)
    plans = plan_db.get_all_plans()
    return render_template(
        'admin.html', plans=plans, token=token, user=current_user
    )

@admin_bp.route(f'/superadmin{token}/edit/<username>', methods=['GET', 'POST'])
@login_required
@role_required('superadmin')
@limiter.limit("10 per minute")
def superadmin_edit_user(username):
    """Full profile edit for a single user.

    Lives under ``/superadmin<token>`` because every field here touches
    identity directly (role, verifications, quota, subscription). Admin
    role no longer has access: the superadmin panel is the only place
    that can rewrite those columns.

    Fields intentionally NOT editable through this form:

    * ``confirmation_token`` — rotated by the resend-confirmation
      endpoint, never hand-edited (a static token cannot expire).
    * ``phone_verification_code`` — same reason, lives in a hashed
      column anyway so even a superadmin should not see it.
    * KEM/SRP blob columns (srp_salt, srp_verifier, public_key,
      encrypted_private_key, kdf_salt) — modifying any of these would
      silently brick the user's login. The server has no UI to rewrite
      them and never should.
    """
    user_db = UserDB(config.SQLALCHEMY_DATABASE_PATH)
    user = user_db.get_user(username)
    if not user:
        flash(f"User {username} not found.", "error")
        return redirect(url_for('admin.superadmin'))

    form = UserEditForm()
    if form.validate_on_submit():
        # ``username`` is DataRequired so ``form.username.data`` is
        # non-None after validation, but Pyright in strict mode still
        # types it as ``str | None``. Collapse the type to ``str``
        # once, here, so the rest of the handler can pass it to the
        # typed DB API.
        target_username = form.username.data or username
        try:
            # Convert storage quota from MB to bytes
            storage_quota_bytes = form.storage_quota.data * 1024 * 1024

            # Parse trial dates if provided
            trial_start = datetime.strptime(form.trial_start.data, '%Y-%m-%d').replace(tzinfo=pytz.UTC) if form.trial_start.data else None
            trial_end = datetime.strptime(form.trial_end.data, '%Y-%m-%d').replace(tzinfo=pytz.UTC) if form.trial_end.data else None

            # Update user fields
            user_db.update_role(
                username=target_username,
                role=form.role.data,
                storage_quota=storage_quota_bytes,
                subscription_status=form.subscription_status.data
            )
            user_db.update_user(
                username=target_username,
                email_verified=form.email_verified.data,
            )
            user_db.update_user_phone_status(
                username=target_username,
                phone_verified=form.phone_verified.data,
            )

            # Update other fields directly
            with sqlite3.connect(config.SQLALCHEMY_DATABASE_PATH) as db:
                db.execute('''
                    UPDATE users SET
                        email = ?,
                        phone = ?,
                        first_name = ?,
                        last_name = ?,
                        trial_start = ?,
                        trial_end = ?
                    WHERE username = ?
                ''', (
                    form.email.data,
                    form.phone.data,
                    form.first_name.data,
                    form.last_name.data,
                    trial_start,
                    trial_end,
                    target_username
                ))
                db.commit()

            flash(f"User {target_username} updated successfully.", "success")
            return redirect(url_for('admin.superadmin'))
        except Exception as e:
            flash(f"Error updating user: {str(e)}", "error")
            return redirect(url_for('admin.superadmin_edit_user', username=username))

    # Pre-fill form with user data
    form.username.data = user['username']
    form.role.data = user['role']
    form.email.data = user['email']
    form.phone.data = user['phone']
    form.first_name.data = user['first_name']
    form.last_name.data = user['last_name']
    form.storage_quota.data = user['storage_quota'] // (1024 * 1024)  # Convert bytes to MB
    form.subscription_status.data = user['subscription_status']
    form.email_verified.data = user['email_verified']
    form.phone_verified.data = user['phone_verified']
    form.trial_start.data = user['trial_start'].strftime('%Y-%m-%d') if user['trial_start'] else ''
    form.trial_end.data = user['trial_end'].strftime('%Y-%m-%d') if user['trial_end'] else ''

    return render_template('superadmin_edit_user.html', form=form, user=user, token=token)

@admin_bp.route(f'/admin{token}/plans', methods=['GET', 'POST'])
@login_required
@role_required('admin', 'superadmin')
@limiter.limit("10 per minute")
def manage_plans():
    """Handle plan management."""
    plan_db = PlanDB(config.SQLALCHEMY_DATABASE_PATH)
    form = PlanForm()
    if form.validate_on_submit():
        try:
            storage_quota_bytes = form.storage_quota.data * 1024 * 1024
            plan_db.create_plan(
                name=form.name.data,
                storage_quota=storage_quota_bytes,
                trial_days=form.trial_days.data,
                price=form.price.data
            )
            flash(f"Plan {form.name.data} created successfully.", "success")
            return redirect(url_for('admin.manage_plans'))
        except Exception as e:
            flash(f"Error creating plan: {str(e)}", "error")
    plans = plan_db.get_all_plans()
    return render_template('manage_plans.html', form=form, plans=plans, token=token)

@admin_bp.route(f'/admin{token}/plans/edit/<plan_name>', methods=['GET', 'POST'])
@login_required
@role_required('admin', 'superadmin')
@limiter.limit("10 per minute")
def edit_plan(plan_name):
    """Handle editing of plan details."""
    plan_db = PlanDB(config.SQLALCHEMY_DATABASE_PATH)
    plan = plan_db.get_plan(plan_name)
    if not plan:
        flash(f"Plan {plan_name} not found.", "error")
        return redirect(url_for('admin.manage_plans'))

    form = PlanForm()
    if form.validate_on_submit():
        try:
            storage_quota_bytes = form.storage_quota.data * 1024 * 1024
            plan_db.update_plan(
                name=plan_name,
                storage_quota=storage_quota_bytes,
                trial_days=form.trial_days.data,
                price=form.price.data
            )
            flash(f"Plan {plan_name} updated successfully.", "success")
            return redirect(url_for('admin.manage_plans'))
        except Exception as e:
            flash(f"Error updating plan: {str(e)}", "error")
            return redirect(url_for('admin.edit_plan', plan_name=plan_name))

    # Pre-fill form with plan data
    form.name.data = plan['name']
    form.storage_quota.data = plan['storage_quota'] // (1024 * 1024)  # Convert bytes to MB
    form.trial_days.data = plan['trial_days']
    form.price.data = plan['price']

    return render_template('edit_plan.html', form=form, plan=plan, token=token)

@admin_bp.route(f'/superadmin{token}', methods=['GET'])
@login_required
@role_required('superadmin')
@limiter.limit("5 per minute")
def superadmin():
    """Superadmin identity-recovery and inventory panel.

    Read-only by design. The server is zero-knowledge, so it can never
    decrypt user content; instead this view surfaces the actions a
    superadmin actually has to perform during incident response:

    * inventory of encrypted file names per user (metadata only)
    * last 50 audit log entries (who did what to which account)
    * the user table with per-row privileged action buttons

    Mutating actions live in the three POST handlers below. The GET
    handler must never accept a side-effect query string, otherwise an
    attacker could trigger a reset by luring a superadmin to follow a
    crafted link.
    """
    user_db = UserDB(config.SQLALCHEMY_DATABASE_PATH)
    file_controller = current_app.file_controller
    audit_db = SuperadminAuditDB(config.SQLALCHEMY_DATABASE_PATH)

    users = user_db.get_all_users()
    # Strip the zero-knowledge blob columns the superadmin panel does
    # not need; shipping them to the template would only inflate the
    # rendered HTML and risk echoing them into logs on error.
    user_rows = [
        {
            "id": u.get("id"),
            "username": u.get("username"),
            "role": u.get("role"),
            "email": u.get("email"),
            "email_verified": bool(u.get("email_verified")),
            "phone": u.get("phone"),
            "phone_verified": bool(u.get("phone_verified")),
            "mfa_enabled": bool(u.get("mfa_enabled")),
            "subscription_status": u.get("subscription_status"),
        }
        for u in users
    ]

    # Encrypted-file inventory: list names per user, not contents.
    # The S3 list is the same call the old panel made, we just don't
    # render a "Download decrypted" button next to each row anymore.
    file_inventory = []
    for u in user_rows:
        try:
            names = file_controller.list_encrypted_files(u["username"])
        except Exception:
            # S3 transient failure should not break the whole panel;
            # an empty inventory for that user is honest enough.
            names = []
        for name in names:
            file_inventory.append({"username": u["username"], "file": name})

    audit_entries = audit_db.recent(limit=50)

    return render_template(
        "superadmin.html",
        users=user_rows,
        files=file_inventory,
        audit=audit_entries,
        token=token,
        user=current_user,
    )


# ---------------------------------------------------------------------------
# Privileged actions
# ---------------------------------------------------------------------------
#
# All three endpoints follow the same shape:
#   1. Resolve the target user. 404 if it does not exist.
#   2. Perform the privileged state change.
#   3. Append a row to the audit log capturing actor, target, IP,
#      and the state transition in the ``details`` field.
#   4. Redirect back to the panel with a flash message.
#
# They are POST-only so a GET cannot trigger a state change. The
# limiter is set tighter than the GET because these endpoints hit
# the database, send mail, and write to the audit log.
# ---------------------------------------------------------------------------

@admin_bp.route(
    f'/superadmin{token}/reset-mfa/<username>', methods=['POST']
)
@login_required
@role_required('superadmin')
@limiter.limit("5 per minute")
def superadmin_reset_mfa(username: str):
    """Disable MFA and clear the pending code for ``username``.

    Used when a user loses their authenticator device. We do NOT
    touch the password, the email, or the KEM material — losing a
    second factor should not invalidate the rest of the identity.
    """
    user_db = UserDB(config.SQLALCHEMY_DATABASE_PATH)
    audit_db = SuperadminAuditDB(config.SQLALCHEMY_DATABASE_PATH)

    user = user_db.get_user(username)
    if not user:
        flash(f"User {username!r} not found.", "error")
        return redirect(url_for('admin.superadmin'))

    was_enabled = bool(user.get("mfa_enabled"))
    try:
        user_db.update_user_mfa_status(
            username=username,
            mfa_code_hash=None,
            mfa_code_expires=None,
            mfa_enabled=False,
        )
    except Exception as exc:
        flash(f"MFA reset failed: {type(exc).__name__}: {exc}", "error")
        return redirect(url_for('admin.superadmin'))

    audit_db.record(
        actor=current_user.username,
        action="reset_mfa",
        target_user=username,
        ip=request.remote_addr,
        details=f"mfa_enabled={was_enabled}->False",
    )
    flash(
        f"MFA cleared for {username!r}. The user will be prompted to "
        f"re-enroll on next login.",
        "success",
    )
    return redirect(url_for('admin.superadmin'))


@admin_bp.route(
    f'/superadmin{token}/resend-confirmation/<username>', methods=['POST']
)
@login_required
@role_required('superadmin')
@limiter.limit("5 per minute")
def superadmin_resend_confirmation(username: str):
    """Issue a fresh ``confirmation_token`` for ``username``.

    The token's 24h expiry is recomputed by ``update_user`` (see
    models/user.py:337). If the user already verified, we still issue
    a new token so the link can be reused as a magic-link login path
    — useful when a user has lost access to their primary device.
    """
    user_db = UserDB(config.SQLALCHEMY_DATABASE_PATH)
    audit_db = SuperadminAuditDB(config.SQLALCHEMY_DATABASE_PATH)

    user = user_db.get_user(username)
    if not user:
        flash(f"User {username!r} not found.", "error")
        return redirect(url_for('admin.superadmin'))

    new_token = secrets.token_urlsafe(32)
    try:
        user_db.update_user(username=username, confirmation_token=new_token)
    except Exception as exc:
        flash(
            f"Could not issue confirmation token: "
            f"{type(exc).__name__}: {exc}",
            "error",
        )
        return redirect(url_for('admin.superadmin'))

    audit_db.record(
        actor=current_user.username,
        action="resend_confirmation",
        target_user=username,
        ip=request.remote_addr,
        details="confirmation_token rotated",
    )
    flash(
        f"New confirmation token issued for {username!r}. "
        f"Surface it via: python scripts/email_tool.py link {username}",
        "success",
    )
    return redirect(url_for('admin.superadmin'))


@admin_bp.route(
    f'/superadmin{token}/toggle-suspend/<username>', methods=['POST']
)
@login_required
@role_required('superadmin')
@limiter.limit("5 per minute")
def superadmin_toggle_suspend(username: str):
    """Flip ``subscription_status`` between active and inactive.

    Suspension is a billing/operational lever (refuse new uploads,
    block new devices) that does not require touching the KEM
    material. Reactivation brings the user back into the same
    position they were in before suspension.
    """
    user_db = UserDB(config.SQLALCHEMY_DATABASE_PATH)
    audit_db = SuperadminAuditDB(config.SQLALCHEMY_DATABASE_PATH)

    user = user_db.get_user(username)
    if not user:
        flash(f"User {username!r} not found.", "error")
        return redirect(url_for('admin.superadmin'))

    previous = user.get("subscription_status") or "active"
    new_status = "inactive" if previous == "active" else "active"
    try:
        user_db.update_role(
            username=username,
            role=user.get("role") or "free",
            storage_quota=user.get("storage_quota") or (10 * 1024 * 1024),
            subscription_status=new_status,
        )
    except Exception as exc:
        flash(
            f"Could not change subscription status: "
            f"{type(exc).__name__}: {exc}",
            "error",
        )
        return redirect(url_for('admin.superadmin'))

    audit_db.record(
        actor=current_user.username,
        action="toggle_suspend",
        target_user=username,
        ip=request.remote_addr,
        details=f"subscription_status={previous}->{new_status}",
    )
    flash(
        f"User {username!r} subscription: {previous} -> {new_status}.",
        "success",
    )
    return redirect(url_for('admin.superadmin'))


@admin_bp.route(f'/admin_contacts{token}', methods=['GET'])
@login_required
@role_required('admin', 'superadmin')
@limiter.limit("5 per minute")
def admin_contacts():
    page = request.args.get('page', 1, type=int)
    if page < 1:
        page = 1
    per_page = 10
    controller = ContactController('instance/users.db')  # Crear instancia directamente
    contacts, total_contacts = controller.contact_db.get_all_contacts(page, per_page)
    total_pages = (total_contacts + per_page - 1) // per_page
    return render_template(
        'admin_contacts.html',
        contacts=contacts,
        page=page,
        total_pages=total_pages,
        per_page=per_page,
        user=current_user
    )
