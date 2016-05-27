from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from mechpy.conta.urls import router as conta_router

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(conta_router.urls)),
    url(r'^admin/', admin.site.urls),
]