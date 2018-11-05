# services/flask_nav.py
from flask import current_app
from flask_nav import Nav, register_renderer
from flask_nav.elements import View, Subgroup
from flask_security import current_user

from .nav import ExtendedNavbar
from .renderers import CustomBootstrapRenderer


nav = Nav()


def secnavbar():
    return ExtendedNavbar(
        title=View(current_app.config.get('SITE_NAME'), 'frontend.index'),
        root_class='navbar navbar-inverse',
        items=(
            View('Home', 'frontend.index'),
        ),
        right_items=(
            View('About', 'frontend.about'),
            Subgroup(
                'Admin',
                View('Admin Page', 'admin.index'),
                View('Log out', 'logout')
            ) if current_user.is_authenticated else View('Log in', 'admin.index')
        )
    )


def get_nav():
    nav.register_element('secnavbar', secnavbar)
    return nav


def register_nav_renderers(server):
    register_renderer(server, 'bootstrap', CustomBootstrapRenderer)
