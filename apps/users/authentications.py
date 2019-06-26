from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from users.models import Token
from rest_framework.exceptions import AuthenticationFailed


class LoginAuthentication(BaseAuthentication):

    def authenticate(self, request):
        """
        Authenticate the request and return a two-tuple of (user, token).
        """
        token = request.META.get('HTTP_AUTHENTICATION')
        if not token:
            raise AuthenticationFailed('请先登录', 0)
        username = Token.objects.filter(token=token).values('username').first()
        if not username:
            raise AuthenticationFailed('用户过期', 0)
        return username, token
