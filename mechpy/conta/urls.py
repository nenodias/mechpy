from django.conf.urls import url, include
from rest_framework import routers

from .views import UserViewSet

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'users', UserViewSet)