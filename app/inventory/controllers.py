from flask_restful import Resource, reqparse


class GetAllInventory(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()

        self.args = parser.parse_args()
        super().__init__()

    def post(self):
        return
