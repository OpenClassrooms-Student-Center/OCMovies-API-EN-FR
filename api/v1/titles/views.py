from rest_framework import generics
from django_filters import rest_framework as filters

from movies.models import Movie
from movies.serializers import MovieListSerializer, MovieDetailSerializer
from .pagination import TitleSetPagination
from .filters import TitleFilterSet


class MovieTitleListView(generics.ListAPIView):
    """
    This endpoint is the main entry point of the **OCMovies API**.

    The OCMovies API is a RESTful API built using Django Rest Framework with
    the objective to support educational projects through a local execution of
    the server. It uses data from more than 80k movies from de IMDb website.

    The actual API opens the
    door to a full exploration of the available movie data without being stuck
    with quotas. Using this main endpoint, you can search data through the use
    of filters. Filters allows to filter and sort data using various criteria
    that can be discovers using the **filter button** on the browserable API
    interface.

    Some detailed info is only available using the detailed info endpoints
    identified with the `url` field.

    If you need to get a full list of available genres, refer to the [genres
    endpoint](/api/v1/genres/).

    """

    http_method_names = ['get']
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = TitleFilterSet
    pagination_class = TitleSetPagination


class MovieTitleDetailView(generics.RetrieveAPIView):
    """
    This endpoint gives access to detailed movie information from the
    **OCMovies API**.

    The OCMovies API is a RESTful API built using Django Rest Framework with
    the objective to support educational projects through a local execution of
    the server. It uses data from more than 80k movies from de IMDb website.

    Not all the detailed data is present in the [title list endpoint available
    here](/api/v1/titles/). Only the detailed information provided on the
    current endpoint gives access to e.g. the description, long description
    or buget and income info about the movie.

    If you need to get a full list of available genres, refer to the [genres
    endpoint](/api/v1/genres/).

    Please, refer to the [title list endpoint](/api/v1/titles/) to get various
    search or sort capabilities, thereby allowing to efficiently identify the
    movies you want to look at.

    """

    http_method_names = ['get']
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer