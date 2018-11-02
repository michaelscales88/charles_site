# services/flask_nav.py
from flask import current_app
from flask_nav import Nav, register_renderer
from flask_bootstrap.nav import BootstrapRenderer
from flask_nav.elements import Navbar, View, Subgroup
from flask_security import current_user


class CustomRenderer(BootstrapRenderer):
    def visit_Navbar(self, node):
        nav_tag = super(CustomRenderer, self).visit_Navbar(node)
        nav_tag['class'] += 'navbar navbar-inverse navbar-fixed-top'
        return nav_tag


def mynavbar():
    return Navbar(
        current_app.config.get('SITE_NAME'),
        View('Home', 'frontend_bp.serve_pages', page='index'),
        View('Contact', 'admin.index'),
        View('About', 'admin.index'),
    )


def secnavbar():
    secnav = list(mynavbar().items)
    if current_user.is_authenticated:
        secnav.extend([
            Subgroup(
                'Admin',
                View('Admin Page', 'admin.index')
            ),
            View('Log out', 'logout')
        ])
    else:
        secnav.extend([
            View('Log in', 'admin.index')
        ])
    return Navbar(current_app.config.get('SITE_NAME'), *secnav)


def get_nav():
    nav = Nav()
    nav.register_element('mynavbar', mynavbar)
    nav.register_element('secnavbar', secnavbar)
    return nav


def add_nav_render(server):
    register_renderer(server, 'custom', CustomRenderer)
