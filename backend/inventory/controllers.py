from flask import jsonify
from flask_restful import Resource
from .models import InventoryModel
from .serializers import inv_table_schema


class GetInventoryTable(Resource):

    def get(self):
        return jsonify(
            data=inv_table_schema.dumps(InventoryModel.all()).data,
            columns=list(inv_table_schema.Meta.fields)
        )
