from backend.extensions import ma
from backend.inventory.models.inventory_model import InventoryModel


class InventorySchema(ma.ModelSchema):
    class Meta:
        fields = ("id", "name", "retail", "description", "quantity")
        model = InventoryModel


class BuyNowSchema(ma.ModelSchema):
    class Meta:
        fields = ("name", "buy_button")
        model = InventoryModel


inv_table_schema = InventorySchema(many=True)
buy_now_schema = BuyNowSchema()
