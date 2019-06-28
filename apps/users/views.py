import uuid

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from clubs.models import Club
from clubs.models import Institute
from clubs.serializers import InstituteSerializer
from users.models import User
from users.models import Token
from users.serializers import UserSerializer
from utils import restful_status
from clubs.serializers import ClubSerializer


class RegisterView(APIView):

    authentication_classes = []

    def post(self, request, *args, **kwargs):
        ret_data = {
            'status': restful_status.STATUS_SUCCESS,
            'msg': ''
        }
        username = request.data.get('username')
        # 用户名已经存在
        if User.objects.filter(username=username).count():
            ret_data['status'] = restful_status.STATUS_ERROR
            ret_data['msg'] = username + ' 用户名已经存在'
            return Response(ret_data)
        # password is md5 code
        password = request.data.get('password')
        nickname = request.data.get('nickname')
        mobile = request.data.get('mobile')
        admission_time = request.data.get('admission_time')
        is_admin = False
        institute_id = request.data.get('institute_id')
        # 注册用户名
        user = User.objects.create(username=username, password=password,
                                   nickname=nickname, is_admin=is_admin, institute_id=institute_id,
                                   mobile=mobile, admission_time=admission_time)
        ret_data['msg'] = username + ' 注册成功'
        return Response(ret_data)


class LoginView(APIView):
    """用户登录 View

    Notes
    -----
    拦截用户的登录 POST 请求, 进行登录
    """

    # 用户登录不需要认证
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        """POST 请求

        Parameters
        ----------
        request : DRF Request 对象

        Returns
        -------
        ret_data : DRF Response
        """
        ret_data = {
            'status': restful_status.STATUS_SUCCESS,
            'msg': ''
        }

        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username, password=password).values('id', 'username')
        if user.count():
            user = user.first()
            token = uuid.uuid4()
            Token.objects.update_or_create(user_id=user.get('id'),
                                           defaults={'user_id': user.get('id'), 'token': token})
            ret_data['msg'] = '登录成功'
            ret_data['username'] = username
            ret_data['userId'] = user.get('id')
            ret_data['token'] = token
            return Response(ret_data)
        ret_data['status'] = restful_status.STATUS_ERROR
        ret_data['msg'] = '用户名或者密码错误'
        return Response(ret_data)


class UserViewSet(GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        ret_data = {
            'status': restful_status.STATUS_SUCCESS
        }
        club_id = request.query_params.get('clubId')
        club = Club.objects.filter(id=club_id).first()
        users = User.objects.filter(clubs=club)
        ret_data['users'] = self.serializer_class(users, many=True).data
        return Response(ret_data)

    def retrieve(self, request, *args, **kwargs):
        ret_data = {
            'status': restful_status.STATUS_SUCCESS
        }
        user_id = request.META.get('PATH_INFO').split('/')[-2]
        queryset = self.queryset
        token = Token.objects.filter(user_id=user_id).values('token').first()
        user = queryset.filter(id=user_id).values('id', 'username',
                                                  'nickname', 'mobile',
                                                  'introduction', 'institute_id',
                                                  'admission_time').first()
        institute_id = user.get('institute_id')
        institute = Institute.objects.filter(id=institute_id).first()
        institute_serializer = InstituteSerializer(institute)
        ret_data['user'] = user
        ret_data['institute'] = institute_serializer.data
        if token.get('token') == request.auth:
            # 已登录用户查看自己信息, 查询社团信息
            clubs = Club.objects.filter(user=queryset.filter(id=user_id).first())
            club_serializer = ClubSerializer(clubs, many=True)
            ret_data['clubs'] = club_serializer.data
        return Response(ret_data)

    def patch(self, request, *args, **kwargs):
        ret_data = {
            'status': restful_status.STATUS_SUCCESS
        }
        user_id = request.META.get('PATH_INFO').split('/')[-2]
        token = Token.objects.filter(user_id=user_id).values('token').first()
        if not token:
            ret_data['status'] = restful_status.STATUS_ERROR
            ret_data['msg'] = '非法携带 token'
            return Response(ret_data)
        if token.get('token') == request.auth:
            user = User.objects.filter(id=user_id).update(**request.data['dict'])
        else:
            ret_data['status'] = restful_status.STATUS_ERROR
            ret_data['msg'] = '非法操作'
        return Response(ret_data)

    def delete(self, request, *args, **kwargs):
        ret_data = {
            'status': restful_status.STATUS_SUCCESS
        }
        user_id = request.META.get('PATH_INFO').split('/')[-2]
        token = Token.objects.filter(user_id=user_id).first()
        if token.token == request.auth:
            token.delete()
        else:
            ret_data['status'] = restful_status.STATUS_ERROR
            ret_data['msg'] = '非法退出'
        return Response(ret_data)