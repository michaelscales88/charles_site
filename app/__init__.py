from flask import Flask

import templates
from .extensions import (
    db, admin, bootstrap, babel, serializer, mail,
    health, moment, register_app_cdn, assets
)

app_instance = Flask(
    __name__,
    template_folder='../templates',
)

import app.core as core

""" Bind Extensions to app """
admin.init_app(app_instance)
babel.init_app(app_instance)
bootstrap.init_app(app_instance)
db.init_app(app_instance)
serializer.init_app(app_instance)
mail.init_app(app_instance)
moment.init_app(app_instance)
health.init_app(app_instance, "/healthcheck")
register_app_cdn(app_instance)
assets.init_app(app_instance)   # Manage JavaScript bundles
templates.nav.init_app(app_instance)

core.after_db_init()

""" Submodule Imports """
import app.inventory


""" Register HTML routes """
app_instance.register_blueprint(templates.frontend_bp)
