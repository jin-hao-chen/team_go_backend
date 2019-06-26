from rest_framework.serializers import Serializer
from rest_framework.serializers import ModelSerializer

from clubs.models import Club


class ClubSerializer(ModelSerializer):

    class Meta:
        model = Club
        fields = ['id', 'name', 'brief', 'icon']
