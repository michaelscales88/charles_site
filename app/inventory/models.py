from app.extensions import db


class InventoryModel(db.Model):

    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    cost = db.Column(db.Float)
    retail = db.Column(db.Float)
    sku = db.Column(db.String)
    description = db.Column(db.Text)


