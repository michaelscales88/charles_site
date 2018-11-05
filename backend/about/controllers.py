from flask import jsonify
from flask_restful import Resource
from .models import AboutPageInfo
from .serializers import about_serializer


class GetAboutPage(Resource):

    def get(self):
        return jsonify(about_serializer.dumps(AboutPageInfo.all()).data)
