import re

from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from clubs.models import Club
from user_operations.models import Apply
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
            clubs = club_serializer.data
            for club in clubs:
                club['applications'] = Apply.objects.filter(club=Club.objects.filter(id=club['id']).first()).count()
            ret_data['clubList'] = clubs
            return Response(ret_data)
        user = User.objects.filter(id=user_id).first()
        if not user:
            ret_data['status'] = restful_status.STATUS_ERROR
            ret_data['msg'] = '此用户不存在'
            return Response(ret_data)
        clubs = queryset.filter(user=user)
        club_serializer = self.serializer_class(clubs, many=True)
        clubs = club_serializer.data
        for club in clubs:
            club['applications'] = Apply.objects.filter(club=Club.objects.filter(id=club['id']).first()).count()
        ret_data['clubList'] = clubs
        return Response(ret_data)

    def patch(self, request, *args, **kwargs):
        ret_data = {
            'status': restful_status.STATUS_SUCCESS
        }
        club_id = int(request.META.get('PATH_INFO').split('/')[-2])
        user = User.objects.filter(username=request.user['username']).first()
        if not user:
            ret_data['status'] = restful_status.STATUS_ERROR
            ret_data['msg'] = '用户' + request.user['username'] + '不存在'
            return Response(ret_data)
        club_ids = UserClub.objects.filter(user=user).values('club_id')
        for club_id_dict in club_ids:
            if club_id == club_id_dict['club_id']:
                club = Club.objects.filter(id=club_id).update(**request.data.get('dict'))
                return Response(ret_data)
        else:
            ret_data['status'] = restful_status.STATUS_ERROR
            ret_data['msg'] = '你没有权限保存内容'
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
        ret_data['required'] = queryset.required
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
