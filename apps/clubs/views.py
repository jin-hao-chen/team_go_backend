from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from clubs.models import Club
from clubs.serializers import ClubSerializer
from utils import restful_status


class ClubListView(GenericViewSet):

    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def list(self, request, *args, **kwargs):
        ret_data = {
            'status': restful_status.STATUS_SUCCESS
        }
        user = request.user
        token = request.auth
        queryset = self.queryset
        club_serializer = self.serializer_class(queryset, many=True)
        ret_data['clubList'] = club_serializer.data
        return Response(ret_data)