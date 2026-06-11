from flask import Blueprint, render_template
from models.plans import PlanDB
faq_bp = Blueprint('faq', __name__)

@faq_bp.route('/faq')
def faq():
    """Render the About page."""
    return render_template('faq.html')

@faq_bp.route('/landing')
def landing():
    """Render the About page."""
    plan_db = PlanDB('instance/users.db')
    plans = plan_db.get_all_plans()

    return render_template('landing.html',plans=plans)
