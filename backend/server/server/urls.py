from django.conf.urls import  include
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from django.conf.urls import url

from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns

urlpatterns = [
    # path("", include("django_nextjs.urls")),
    path('admin/', admin.site.urls),
    # path("", include("apps.endpoints.urls")),
    # path("", include("django_nextjs.urls")),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

urlpatterns += endpoints_urlpatterns