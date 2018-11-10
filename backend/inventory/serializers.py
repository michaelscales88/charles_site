from marshmallow import fields
from ..extensions import ma
from .models import InventoryModel


class CurrencyField(fields.Field):
    """Field that serializes to a title case string and deserializes
    to a lower case string.
    """
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return ''
        return value.title()

    def _deserialize(self, value, attr, data, **kwargs):
        return value.lower()


class InventorySchema(ma.ModelSchema):
    stock = fields.Method("buy_now_quantity")

    class Meta:
        fields = ("id", "name", "retail", "stock")
        model = InventoryModel

    @staticmethod
    def buy_now_quantity(obj):
        return obj.quantity if obj.quantity > 0 else 0


class BuyNowSchema(ma.ModelSchema):
    buttons = fields.Method('buy_now_button')

    class Meta:
        fields = ("name", "path", "retail", "buttons", "description")
        model = InventoryModel

    @staticmethod
    def buy_now_button(obj):
        return obj.buy_button if obj.quantity > 0 else "Out of Stock"


inv_table_schema = InventorySchema(many=True)
buy_now_schema = BuyNowSchema()
