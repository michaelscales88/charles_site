# templates/frontend.py
from flask import Blueprint, render_template, request, redirect, url_for

from .navbar import get_nav, register_nav_renderers

frontend_bp = Blueprint('frontend', __name__)


@frontend_bp.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'), code=302)


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


@frontend_bp.route("/order/success")
def order_success():
    return render_template(
        'pages/order_status.html',
        title='Order Success',
        status="success",
        id=request.args.get("id")
    )


@frontend_bp.route("/order/cancel")
def order_cancel():
    return render_template(
        'pages/order_status.html',
        title='Cancellation Page',
        status="cancel",
        id=request.args.get("id")
    )
