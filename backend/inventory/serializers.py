from backend.extensions import ma
from backend.inventory.models.inventory_model import InventoryModel


class InventorySchema(ma.ModelSchema):
    class Meta:
        fields = ("name", "retail", "description", "quantity")
        model = InventoryModel


inv_table_schema = InventorySchema(many=True)
