from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from mechpy.conta.urls import router as conta_router

urlpatterns = [
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(conta_router.urls)),
    #url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]