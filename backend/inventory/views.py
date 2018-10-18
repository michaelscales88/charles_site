from backend.base_view import BaseView


class InventoryView(BaseView):
    column_list = ("name", "retail", "quantity")


class InventoryStockView(BaseView):
    pass


class SalesView(BaseView):
    pass
