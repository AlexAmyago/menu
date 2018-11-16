from django.contrib import admin
from django.urls import path
from .spot_menu.urls import urlpatterns as spot_urls

urlpatterns = [
    path('admin/', admin.site.urls),
] + spot_urls
