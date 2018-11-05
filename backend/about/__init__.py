from flask import Blueprint
from flask_restful import Api

from backend import server, db
from backend.core import build_routes
from backend.extensions import admin

about_bp = Blueprint('about_bp', __name__)
about_api = Api(about_bp)

with server.app_context():
    import backend.about.models
    import backend.about.views
    db.create_all()

    admin.add_view(
        views.AboutImageView(
            models.AboutImageModel, db.session,
            name='About Images', category='About Page'
        )
    )
    admin.add_view(
        views.AboutView(
            models.AboutPageInfo, db.session,
            name='About Info', category='About Page'
        )
    )

    # Inject module routes
    build_routes(server, about_api, "about")

    server.register_blueprint(about_bp)
