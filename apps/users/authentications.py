from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import APIException

from users.models import Token
from users.models import User


class LoginError(APIException):
    pass


class LoginAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.META.get('HTTP_TOKEN')
        if not token:
            raise LoginError('请先登录')
        user_id = Token.objects.filter(token=token).values('user_id')
        if not user_id:
            raise LoginError('用户过期')
        username = User.objects.filter(id=user_id.first().get('user_id')).values('username').first()
        return username, token
