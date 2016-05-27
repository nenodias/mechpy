from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import authentication
from rest_framework import exceptions

User = get_user_model()

class AppAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        user = None
        key_token = request.META.get('HTTP_AUTHORIZATION')
        if key_token:
            key_token = key_token.replace('Token ', '')
        try:
            token = Token.objects.get(key=key_token)
            user = token.user
        except:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)