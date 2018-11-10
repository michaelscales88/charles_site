from flask import jsonify, abort
from flask_restful import Resource, reqparse
from .models import InventoryModel
from .serializers import inv_table_schema, buy_now_schema


class GetInventoryTable(Resource):

    def get(self):
        view_columns = list(inv_table_schema.Meta.fields)
        view_columns.pop(0)     # Remove id from the view
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
            return jsonify(buy_now_schema.dumps(inventory_model).data)
        else:
            return abort(404, "No inventory exists for model id: {id}".format(id=self.args['id']))


class OrderStatus(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int)
        self.args = parser.parse_args()

    def post(self):
        inventory_model = InventoryModel.find(self.args['id'])
        if inventory_model:
            return jsonify(200, "success")
        else:
            return abort(404, "No inventory exists for model id: {id}".format(id=self.args['id']))

    def delete(self):
        inventory_model = InventoryModel.find(self.args['id'])
        if inventory_model:
            return jsonify(200, "deleted")
        else:
            return abort(404, "No inventory exists for model id: {id}".format(id=self.args['id']))

