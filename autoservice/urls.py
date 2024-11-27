from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('autoservice/', include('autoservice.urls')),
    path('admin/', admin.site.urls),
]