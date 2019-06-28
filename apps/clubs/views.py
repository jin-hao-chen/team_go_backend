import re

from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from clubs.models import Club
from clubs.models import Institute
from clubs.models import UserClub
from clubs.serializers import UserClubSerializer
from users.models import User
from clubs.serializers import ClubSerializer
from clubs.serializers import InstituteSerializer
from utils import restful_status
from utils import model_tools


class InstituteViewSet(GenericViewSet):

    authentication_classes = []

    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer

    def list(self, request, *args, **kwargs):
        ret_data = {
            'status': restful_status.STATUS_SUCCESS
        }
        queryset = self.queryset
        institute_serializer = self.serializer_class(queryset, many=True)
        ret_data['instituteList'] = institute_serializer.data
        return Response(ret_data)

    def retrieve(self, request, *args, **kwargs):
        institute_id = request.META.get('PATH_INFO').split('/')[-2]
        ret_data = {
            'status': restful_status.STATUS_SUCCESS
        }
        queryset = self.queryset
        institute = queryset.filter(id=institute_id).first()
        institute_serializer = self.serializer_class(institute, many=False)
        ret_data['institute'] = institute_serializer.data
        return Response(ret_data)


class ClubListViewSet(GenericViewSet):

    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def list(self, request, *args, **kwargs):
        ret_data = {
            'status': restful_status.STATUS_SUCCESS
        }
        queryset = self.queryset.order_by('-persons')
        user_id = request.query_params.get('userId')
        if not user_id:
            club_serializer = self.serializer_class(queryset, many=True)
            ret_data['clubList'] = club_serializer.data
            return Response(ret_data)
        user = User.objects.filter(id=user_id).first()
        if not user:
            ret_data['status'] = restful_status.STATUS_ERROR
            ret_data['msg'] = '此用户不存在'
            return Response(ret_data)
        clubs = queryset.filter(user=user)
        club_serializer = self.serializer_class(clubs, many=True)
        ret_data['clubList'] = club_serializer.data
        return Response(ret_data)

    def retrieve(self, request, *args, **kwargs):
        # 请求的 URL 在 request.META.PATH_INFO 中
        club_id = request.META.get('PATH_INFO').split('/')[-2]
        ret_data = {
            'status': restful_status.STATUS_SUCCESS
        }
        queryset = self.queryset.filter(id=club_id).first()
        description = queryset.description
        ret_data['description'] = description
        return Response(ret_data)


class UserClubViewSet(GenericViewSet):

    queryset = UserClub.objects.all()
    serializer_class = UserClubSerializer

    def list(self, request, *args, **kwargs):
        ret_data = {
            'status': restful_status.STATUS_SUCCESS
        }
        user_id = request.query_params.get('userId')
        queryset = self.queryset
        user = User.objects.filter(id=user_id).first()
        if not user:
            ret_data['status'] = restful_status.STATUS_ERROR
            ret_data['msg'] = '非法请求'
            return Response(ret_data)
        user_club = queryset.filter(user=user)
        ret_data['user_club'] = self.serializer_class(user_club, many=True).data
        return Response(ret_data)
