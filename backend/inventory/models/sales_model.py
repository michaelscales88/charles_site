import datetime
from sqlalchemy import func
from backend.extensions import db


class SalesModel(db.Model):
    __tablename__ = "sales"

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    sale_date = db.Column(db.DateTime(), default=datetime.datetime.utcnow())

    type_id = db.Column(db.Integer, db.ForeignKey("inventory.id"))
    type = db.relationship("InventoryModel")

    @classmethod
    def get_quantity(cls, foreign_id):
        quantity = cls.session.query(
            func.sum(cls.quantity)
        ).filter(
            cls.type_id == foreign_id
        ).scalar()
        return quantity if quantity else 0
