from flask import jsonify, abort
from flask_restful import Resource, reqparse
from .models import InventoryModel
from .serializers import inv_table_schema, buy_now_schema


class GetInventoryTable(Resource):

    def get(self):
        view_columns = list(inv_table_schema.Meta.fields)
        view_columns.pop(0)     # Remove id from the view
        view_columns.pop(2)     # Remove description from the view
        return jsonify(
            data=inv_table_schema.dumps(InventoryModel.all()).data,
            columns=view_columns
        )


class GetBuyNowInfo(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int)
        self.args = parser.parse_args()

    def post(self):
        inventory_model = InventoryModel.find(self.args['id'])
        if inventory_model:
            buy_info = buy_now_schema.dumps(inventory_model).data
            return jsonify(buy_info)
        else:
            return abort(404, "No inventory exists for model id: {id}".format(id=self.args['id']))
