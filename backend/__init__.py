from flask import Flask
from flask_assets import Bundle

import frontend
from .extensions import (
    db, admin, boot, babel, cors, ma, mail,
    health, moment, register_app_cdn, assets, debugger
)

server = Flask(
    __name__,
    template_folder='../frontend',
    static_folder="../static"
)

# Application Security
import backend.core as core

""" Bind Extensions to app """
admin.init_app(server)
babel.init_app(server)
boot.init_app(server)
cors.init_app(server)
ma.init_app(server)
mail.init_app(server)
moment.init_app(server)
health.init_app(server, "/healthcheck")
assets.init_app(server)

""" Submodule Imports """
import backend.inventory


""" Register HTML """
register_app_cdn(server)
# Add server's static files to be bundled and minified
js = Bundle(
    'js/gridArea.js',
    filters='jsmin', output='gen/packed.js'
)
css = Bundle(
    'css/style.css',
    filters='cssmin', output='gen/all.css'
)
assets.register('js_all', js)
assets.register('css_all', css)
nav = frontend.get_nav()
nav.init_app(server)
frontend.add_nav_render(server)
server.register_blueprint(frontend.frontend_bp)

if server.config.get("DEBUG", False):
    debugger.init_app(server)
