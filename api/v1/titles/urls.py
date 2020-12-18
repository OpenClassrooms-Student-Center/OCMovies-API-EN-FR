from django.urls import path

from .views import MovieTitleListView, MovieTitleDetailView

urlpatterns = [
    path('', MovieTitleListView.as_view(), name="movie-list"),
    path('<int:pk>', MovieTitleDetailView.as_view(), name="movie-detail"),
]
