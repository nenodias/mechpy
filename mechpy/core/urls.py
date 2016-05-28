from django.conf.urls import url, include
from rest_framework import routers

from .views import PaisViewSet, EstadoViewSet, CidadeViewSet, PessoaViewSet

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'paises', PaisViewSet)
router.register(r'estados', EstadoViewSet)
router.register(r'cidades', CidadeViewSet)
router.register(r'pessoas', PessoaViewSet)