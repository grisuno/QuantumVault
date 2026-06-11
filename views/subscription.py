import os
from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_required, current_user
from models.user import UserDB
from models.plans import PlanDB
import paypalrestsdk
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .auth import role_required

subscription_bp = Blueprint('subscription', __name__)
limiter = Limiter(key_func=get_remote_address)

# Configurar PayPal en modo sandbox
paypalrestsdk.configure({
    "mode": "live",
    "client_id": "ARiFGf3NhZsNZnlToWteCHpZkCKE31chajDadW-BZ9g8PusPRoABHTH0djs1j2tGhF0ZrCnemB1dDxeS",
    "client_secret": "EP1WS2tCFcRU9e2Lqw9p-Ow5vwsr7sVT3FWcMH3LTVwKqbt_4BSZJhTx_rTEKKXVAGKomozTIQz-l2DT"
})

class SubscriptionForm(FlaskForm):
    """Formulario para seleccionar un plan de suscripción."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        plan_db = PlanDB('instance/users.db')
        plans = plan_db.get_all_plans()
        self.plan.choices = [(plan['name'], f"{plan['name'].capitalize()} (${plan['price']}/mes)") for plan in plans if plan['name'] != 'free']

    plan = SelectField('Subscription Plan', validators=[DataRequired()])
    submit = SubmitField('Subscribe')

@subscription_bp.route('/subscribe', methods=['GET', 'POST'])
@limiter.limit("10 per minute")
def subscribe():
    """Maneja la selección de planes y el proceso de pago."""
    form = SubscriptionForm()
    if request.method == 'POST' and form.validate_on_submit():
        if not current_user.is_authenticated:
            flash('You must log in to subscribe.')
            return redirect(url_for('auth.login'))

        plan_name = form.plan.data
        plan_db = PlanDB('instance/users.db')
        plan = plan_db.get_plan(plan_name)
        if not plan:
            flash('Invalid plan selected.')
            return redirect(url_for('subscription.subscribe'))

        # Guardar el plan seleccionado en la sesión
        session['pending_plan'] = plan_name

        try:
            payment = paypalrestsdk.Payment({
                "intent": "sale",
                "payer": {"payment_method": "paypal"},
                "transactions": [{
                    "amount": {
                        "total": f"{plan['price']:.2f}",
                        "currency": "USD"
                    },
                    "description": f"Plan subscription {plan_name} of QuantumVault"
                }],
                "redirect_urls": {
                    "return_url": url_for('subscription.payment_success', _external=True),
                    "cancel_url": url_for('subscription.subscribe', _external=True)
                }
            })

            if payment.create():
                for link in payment.links:
                    if link.rel == "approval_url":
                        return redirect(link.href)
            else:
                flash("Error starting payment with PayPal")
        except Exception as e:
            flash(f"Error processing payment: {str(e)}")

    return render_template('subscribe.html', form=form, user=current_user)

@subscription_bp.route('/payment/success')
@login_required
@limiter.limit("10 per minute")
def payment_success():
    """Maneja el éxito del pago y actualiza el plan del usuario."""
    payment_id = request.args.get('paymentId')
    payer_id = request.args.get('PayerID')
    plan_name = request.args.get('plan')

    # Verificar que el plan esté en la sesión
    pending_plan = session.get('pending_plan')
    if not payment_id or not payer_id or not pending_plan:
        flash("Invalid payment parameters or session expired")
        return redirect(url_for('subscription.subscribe'))

    # Validar que el plan de la URL no fue manipulado
    if plan_name and plan_name != pending_plan:
        flash("Plan mismatch detected. Possible tampering attempt.")
        return redirect(url_for('subscription.subscribe'))

    try:
        payment = paypalrestsdk.Payment.find(payment_id)
        plan_db = PlanDB('instance/users.db')
        # Verificar que el monto pagado coincide con el plan
        amount_paid = float(payment.transactions[0].amount.total)
        if not plan_db.validate_plan_payment(pending_plan, amount_paid):
            flash("Payment amount does not match the selected plan.")
            return redirect(url_for('subscription.subscribe'))

        if payment.execute({"payer_id": payer_id}):
            user_db = UserDB('instance/users.db')
            plan = plan_db.get_plan(pending_plan)
            user_db.update_role(
                username=current_user.username,
                role=pending_plan,
                storage_quota=plan["storage_quota"],
                subscription_status="active"
            )
            flash(f"Plan subscription {pending_plan} successfully activated")
            # Limpiar la sesión
            session.pop('pending_plan', None)
            return redirect(url_for('views.home'))
        else:
            flash("Error executing payment")
    except Exception as e:
        flash(f"Error processing payment: {str(e)}")

    return redirect(url_for('subscription.subscribe'))
