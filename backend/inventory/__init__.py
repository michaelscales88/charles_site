from flask import Blueprint
from flask_restful import Api

from backend import server, db
from backend.core import build_routes
from backend.extensions import admin

inventory_bp = Blueprint('inventory_bp', __name__)
inventory_api = Api(inventory_bp)

with server.app_context():
    import backend.inventory.models
    import backend.inventory.views
    db.create_all()

    admin.add_view(
        views.InventoryView(
            models.InventoryModel, db.session,
            name='View Inventory', category='Manage Inventory'
        )
    )
    admin.add_view(
        views.InventoryStockView(
            models.InventoryStockModel, db.session,
            name='Change Stock', category='Manage Inventory'
        )
    )
    admin.add_view(
        views.SalesView(
            models.SalesModel, db.session,
            name='View Sales', category='Manage Inventory'
        )
    )

    # Inject module routes
    build_routes(server, inventory_api, "inventory")

    server.register_blueprint(inventory_bp)

