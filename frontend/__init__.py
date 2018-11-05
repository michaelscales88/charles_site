# templates/frontend.py
from flask import Blueprint, render_template

from .navbar import get_nav, register_nav_renderers

frontend_bp = Blueprint('frontend', __name__)


@frontend_bp.route("/")
def index():
    return render_template(
        'pages/index.html',
        title='Home'
    )


@frontend_bp.route("/about")
def about():
    return render_template(
        'pages/about.html',
        title='About Us'
    )
