# app/extensions.py
from flask_assets import Environment
from flask_admin import Admin
from flask_babel import Babel
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from .cdn_registration import register_app_cdn
from ..base_model import BaseModel

# Services
admin = Admin(template_mode='bootstrap3', base_template="admin_layout.html")
babel = Babel()
db = SQLAlchemy(model_class=BaseModel)  # Database manager
mail = Mail()                           # Mailer
boot = Bootstrap()                      # Styles
ma = Marshmallow()                      # Serializer
assets = Environment()                  # Static JS bundling and minification
debugger = DebugToolbarExtension()
