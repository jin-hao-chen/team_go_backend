from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from user_operations.models import Apply
from users.serializers import UserSerializer
from clubs.serializers import ClubSerializer
from user_operations.serializers import ApplySerializer
from users.models import User
from clubs.models import Club
from clubs.models import UserClub
from utils import restful_status


class ApplyViewSet(GenericViewSet):

    queryset = Apply.objects.all()
    serializer_class = ApplySerializer
    authentication_classes = []

    def delete(self, request, *args, **kwargs):
        ret_data = {
            'status': restful_status.STATUS_SUCCESS
        }
        application_id = request.data.get('applicationId')
        club_id = request.data.get('clubId')
        accept = request.data.get('accept')
        queryset = self.queryset
        user = User.objects.filter(id=application_id).first()
        club = Club.objects.filter(id=club_id).first()
        queryset.filter(user=user, club=club).delete()
        if accept:
            # 添加人数
            persons = int(Club.objects.filter(id=club_id).values('persons').first().get('persons')) + 1
            Club.objects.filter(id=club_id).update(persons=persons)
            club = Club.objects.filter(id=club_id)
            user.clubs.add(*club)
        return Response(ret_data)

    def list_user(self, club_id):
        club = Club.objects.filter(id=club_id).first()
        queryset = self.queryset
        user_club = queryset.filter(club=club).values('user_id', 'department_name')
        users_info = []
        for uc in user_club:
            user_id = uc.get('user_id')
            user = UserSerializer(User.objects.filter(id=user_id).first()).data
            user['department'] = queryset.filter(club=Club.objects.filter(id=club_id).first()).values(
                'department_name').first().get('department_name')
            users_info.append(user)
        return users_info

    def list_club(self, user_id):
        user = User.objects.filter(id=user_id).first()
        queryset = self.queryset
        user_club = queryset.filter(user=user).values('club_id', 'department_name')
        clubs_info = []
        for uc in user_club:
            club_id = uc.get('club_id')
            club = ClubSerializer(Club.objects.filter(id=club_id).first()).data
            club['department'] = queryset.filter(user=User.objects.filter(id=user_id).first()).values(
                'department_name').first().get('department_name')
            clubs_info.append(club)
        return clubs_info

    def list(self, request, *args, **kwargs):
        ret_data = {
            'status': restful_status.STATUS_SUCCESS
        }
        club_id = request.query_params.get('clubId')
        user_id = request.query_params.get('userId')
        if club_id:
            ret_data['applications'] = self.list_user(club_id)
        elif user_id:
            ret_data['applicationClubs'] = self.list_club(user_id)
        return Response(ret_data)

    def create(self, request, *args, **kwargs):
        ret_data = {
            'status': restful_status.STATUS_SUCCESS
        }
        user_id = int(request.data['userId'])
        club_id = int(request.data['clubId'])
        department_name = request.data['department']
        queryset = self.queryset
        user = User.objects.filter(id=user_id).first()
        club = Club.objects.filter(id=club_id).first()

        user_club = UserClub.objects.filter(user=user, club=club)
        if user_club.count():
            ret_data['status'] = restful_status.STATUS_ERROR
            ret_data['msg'] = '你已经是该社团的管理员'
            return Response(ret_data)

        joined_club_ids = Club.objects.filter(user=user).values('id')
        for joined_club_id in joined_club_ids:
            if joined_club_id['id'] == club_id:
                ret_data['status'] = restful_status.STATUS_ERROR
                ret_data['msg'] = '你已经加入了该社团'
                return Response(ret_data)
        apply = Apply.objects.filter(user=user, club=club).first()
        if apply:
            ret_data['status'] = restful_status.STATUS_ERROR
            ret_data['msg'] = '你已经申请过了'
            return Response(ret_data)

        Apply.objects.create(user=user, club=club, department_name=department_name)
        return Response(ret_data)
