from rest_framework.serializers import ModelSerializer

from clubs.models import Club
from clubs.models import Institute
from clubs.models import UserClub


class ClubSerializer(ModelSerializer):

    class Meta:
        model = Club
        fields = ['id', 'name', 'brief', 'icon', 'persons']


class InstituteSerializer(ModelSerializer):

    class Meta:
        model = Institute
        fields = '__all__'


class UserClubSerializer(ModelSerializer):

    class Meta:
        model = UserClub
        fields = '__all__'
