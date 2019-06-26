import uuid

from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import User
from users.models import Token
from utils import restful_code


class RegisterView(APIView):

    def post(self, request, *args, **kwargs):
        status_code = 0
        ret_data = {
            'detail': ''
        }
        username = request.data.get('username')
        # password is md5 code
        password = request.data.get('password')
        nickname = request.data.get('nickname')
        mobile = request.data.get('mobile')
        is_admin = False
        institute_id = request.data.get('institute_id')
        # User.objects.create()


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
        status_code = restful_code.CODE_SUCCESS
        ret_data = {
            'detail': ''
        }

        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username, password=password).values('id', 'username')
        if user.count():
            user = user.first()
            token = uuid.uuid4()
            Token.objects.update_or_create(user_id=user.get('id'),
                                           defaults={'user_id': user.get('id'), 'token': token})
            ret_data['detail'] = '登录成功'
            ret_data['username'] = username
            return Response(ret_data, status=status_code)
        status_code = restful_code.CODE_ERROR
        ret_data['detail'] = '用户名或者密码错误'
        return Response(ret_data, status=status_code)

