from ..extensions import ma
from .models import AboutPageInfo


class AboutInfoSerializer(ma.ModelSchema):
    class Meta:
        fields = ("title", "description", "path")
        model = AboutPageInfo


about_serializer = AboutInfoSerializer(many=True)
