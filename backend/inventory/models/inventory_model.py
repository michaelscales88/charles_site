from flask_admin import form
from backend.extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from .sales_model import SalesModel
from .inventory_stock_model import InventoryStockModel


class InventoryModel(db.Model):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    cost = db.Column(db.Float)
    retail = db.Column(db.Float)
    sku = db.Column(db.String)
    description = db.Column(db.Text)
    buy_button = db.Column(db.Text)

    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))
    image = db.relationship("ImageModel", back_populates="inventory")

    def __str__(self):
        return self.name

    @hybrid_property
    def path(self):
        return form.thumbgen_filename(self.image.path)

    @hybrid_property
    def quantity(self):
        return abs(
            InventoryStockModel.get_quantity(self.id)
            - SalesModel.get_quantity(self.id)
        )
