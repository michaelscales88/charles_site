# security/__init__.py
from flask import url_for
from flask_admin import helpers
from flask_security import Security, SQLAlchemyUserDatastore
from flask_security.utils import hash_password

from backend import server
from backend.extensions import admin, db
from .models import UserModel, RolesModel
from .utilities import ExtendedLoginForm, ExtendedRegisterForm


user_datastore = SQLAlchemyUserDatastore(db, UserModel, RolesModel)
security = Security(
    server, user_datastore,
    login_form=ExtendedLoginForm,
    register_form=ExtendedRegisterForm
)


# Create a user to test with
@server.before_first_request
def create_user():
    if not UserModel.find(1):
        user_datastore.create_role(name="user")
        user_datastore.create_role(name="superuser")

        user_datastore.create_user(
            username='admin',
            password=hash_password('password'),
            roles=["superuser"]
        )

        db.session.commit()


@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=helpers,
        get_url=url_for
    )
