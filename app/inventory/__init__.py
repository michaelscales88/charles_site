from flask import Blueprint
from flask_restful import Api

from app import app_instance, db
from app.core import build_routes
from app.extensions import admin
from .models import InventoryModel
from .views import InventoryView

inventory_bp = Blueprint('inventory_bp', __name__)
inventory_api = Api(inventory_bp)

with app_instance.app_context():
    db.create_all()

    admin.add_view(InventoryView(InventoryModel, db.session))

# Inject module routes
build_routes(app_instance, inventory_api, "inventory")
