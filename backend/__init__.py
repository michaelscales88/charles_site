from flask import Flask
from flask_assets import Bundle

import frontend
from .extensions import (
    db, admin, boot, babel, ma, mail,
    register_app_cdn, assets, debugger
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
debugger.init_app(server)
ma.init_app(server)
mail.init_app(server)
assets.init_app(server)

""" Submodule Imports """
import backend.about
import backend.inventory


""" Register HTML """
# Register external CDNs
register_app_cdn(server)

# Add server's static files to be bundled and minified
js = Bundle(
    'js/aboutPage.js',
    'js/gridArea.js',
    'js/buyNow.js',
    'js/backToTop.js',
    'js/main.js',
    'js/util.js',
    filters='jsmin', output='gen/packed.js'
)
css = Bundle(
    'css/font-awesome.min.css',
    'css/main.css',
    filters='cssmin', output='gen/all.css'
)
assets.register('js_all', js)
assets.register('css_all', css)

# Register HTML endpoints
server.register_blueprint(frontend.frontend_bp)
