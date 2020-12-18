"""OCMovies-API URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/genres/', include('api.v1.genres.urls')),
    path('api/v1/titles/', include('api.v1.titles.urls')),
]
