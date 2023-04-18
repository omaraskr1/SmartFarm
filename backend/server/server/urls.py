from django.conf.urls import  include
from django.contrib import admin
from django.urls import path

from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns

urlpatterns = [
    # path("", include("django_nextjs.urls")),
    path('admin/', admin.site.urls),
    # path("", include("apps.endpoints.urls")),
    # path("", include("django_nextjs.urls")),
]

urlpatterns += endpoints_urlpatterns