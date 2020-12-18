from django_filters import rest_framework as filters

from movies.models import Genre


class GenreFilterSet(filters.FilterSet):
    """Implements filters to be used with TitleListView."""

    name_contains = filters.CharFilter(
        field_name="name", lookup_expr='icontains'
    )
    movie_title_contains = filters.CharFilter(
        field_name="movies", lookup_expr='title__icontains'
    )

    class Meta:
        model = Genre
        fields = ['name']