from django.core.urlresolvers import resolve
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token
from rest_framework import authentication
from rest_framework import exceptions

from django.conf import settings

User = get_user_model()

class AppAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        match = resolve(request._request.path)
        if settings.TOKEN_URL != match.url_name:
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
        else:
            return (AnonymousUser(), None)
