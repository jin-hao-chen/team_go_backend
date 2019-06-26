import uuid

from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import User
from users.models import Token
from utils import restful_status


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
            ret_data['token'] = token
            return Response(ret_data)
        ret_data['status'] = restful_status.STATUS_ERROR
        ret_data['msg'] = '用户名或者密码错误'
        return Response(ret_data)
