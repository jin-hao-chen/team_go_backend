from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.serializers import ModelSerializer

from clubs.models import Club
from clubs.models import Institute
from clubs.models import UserClub


class ClubSerializer(ModelSerializer):

    type = serializers.ChoiceField(choices=Club.TYPE_CHOICES, source="get_type_display")
    level = serializers.ChoiceField(choices=Club.LEVEL_CHOICES, source="get_level_display")
    required = serializers.ChoiceField(choices=Club.REQUIRED_CHOICE, source='get_required_display')

    class Meta:
        model = Club
        fields = ['id', 'name', 'brief', 'icon', 'persons', 'type', 'level', 'required']


class InstituteSerializer(ModelSerializer):

    class Meta:
        model = Institute
        fields = '__all__'


class UserClubSerializer(ModelSerializer):

    class Meta:
        model = UserClub
        fields = '__all__'
