# templates/frontend.py
from flask import Blueprint, render_template

from .navbar import get_nav, register_nav_renderers

frontend_bp = Blueprint('frontend', __name__)


@frontend_bp.route("/")
def index():
    return render_template(
        'index.html',
        title='Home'
    )
