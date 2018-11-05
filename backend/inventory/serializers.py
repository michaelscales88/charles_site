from marshmallow import fields
from backend.extensions import ma
from backend.inventory.models.inventory_model import InventoryModel


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
    class Meta:
        fields = ("id", "name", "retail", "quantity")
        model = InventoryModel


class BuyNowSchema(ma.ModelSchema):
    class Meta:
        fields = ("name", "path", "retail", "buy_button", "description")
        model = InventoryModel


inv_table_schema = InventorySchema(many=True)
buy_now_schema = BuyNowSchema()
