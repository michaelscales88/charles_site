from flask import jsonify
from flask_restful import Resource


class GetAboutPage(Resource):

    def get(self):
        return jsonify()