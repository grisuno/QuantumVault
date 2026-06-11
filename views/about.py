from flask import Blueprint, render_template

about_bp = Blueprint('about', __name__)

@about_bp.route('/about')
def about():
    """Render the About page."""
    return render_template('about.html')
