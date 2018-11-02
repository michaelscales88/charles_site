# security/__init__.py
from flask import url_for, Blueprint, flash, redirect
from flask_restful import Api
from flask_security import logout_user

from backend import server
from backend.extensions import admin, db
from backend.base_model import BaseModel

from .route_builder import build_routes
from .utilities import ExtendedLoginForm, ExtendedRegisterForm

# Configure app settings
import backend.core.config_runner

db.init_app(server)
BaseModel.set_session(db.session)

import backend.core.security

security_bp = Blueprint('user_bp', __name__)
security_api = Api(security_bp)


@server.route("/logout")
def logout():
    logout_user()
    flash("Logged out!")
    return redirect(url_for("frontend_bp.serve_pages", page="index"))


with server.app_context():
    import backend.core.models
    import backend.core.views

    # Creates any models that have been imported
    db.create_all()

    # Register the admin views to the extension
    admin.add_view(
        views.UsersView(
            models.UserModel, db.session, name='Manage Users', category='User Admin'
        )
    )
    admin.add_view(
        views.RolesView(
            models.RolesModel, db.session, name='Manage Privileges', category='User Admin'
        )
    )


server.register_blueprint(security_bp)
