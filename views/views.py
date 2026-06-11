"""Top-level non-API views: home page, account preferences, etc."""

from flask import Blueprint, render_template
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField

from models.user import UserDB


views_bp = Blueprint("views", __name__)


class MFAEnableForm(FlaskForm):
    mfa_enabled = BooleanField("Enable Two-Factor Authentication (2FA)")
    submit = SubmitField("Save")


@views_bp.route("/")
def home():
    """Render the landing/home page.

    The total user count is fetched with ``SELECT COUNT(*)`` directly
    rather than loading every row into memory, so the cost is O(1)
    regardless of the user table size.
    """
    user_db = UserDB("instance/users.db")
    number_users = user_db.count_users()
    form = MFAEnableForm()
    return render_template("home.html", user=current_user, number_users=number_users, form=form)
