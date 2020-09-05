"""
Proyecto Curso Django
"""
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.home.urls')),
]