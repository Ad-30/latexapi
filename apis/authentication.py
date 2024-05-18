from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import AnonymousUser
class AccessKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        access_key = request.headers.get('X-Access-Key')
        if not access_key:
            raise AuthenticationFailed('Access key missing')

        if access_key != settings.ACCESS_KEY:
            print(settings.ACCESS_KEY)
            raise AuthenticationFailed('Invalid access key')

        return (AnonymousUser(), None)