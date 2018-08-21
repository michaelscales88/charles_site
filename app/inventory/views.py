from app.base_view import BaseView


class InventoryView(BaseView):
    column_searchable_list = ("sku",)
    pass
