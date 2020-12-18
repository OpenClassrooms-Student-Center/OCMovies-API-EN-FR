from django.urls import path

from .views import GenreListView

urlpatterns = [
    path('', GenreListView.as_view(), name="genre-list"),
]
