from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('me/', include('me.urls')),
    path('admin/', admin.site.urls),
]