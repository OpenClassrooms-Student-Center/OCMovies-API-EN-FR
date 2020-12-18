from django_filters import rest_framework as filters

from movies.models import Movie


class TitleFilterSet(filters.FilterSet):
    """Implements filters to be used with TitleListView."""

    min_year = filters.NumberFilter(field_name="year", lookup_expr='gte')
    max_year = filters.NumberFilter(field_name="year", lookup_expr='lte')
    imdb_score_min = filters.NumberFilter(
        field_name="imdb_score", lookup_expr='gte'
    )
    imdb_score_max = filters.NumberFilter(
        field_name="imdb_score", lookup_expr='lte'
    )
    title_contains = filters.CharFilter(
        field_name="title", lookup_expr='icontains'
    )
    director = filters.CharFilter(
        field_name="directors", lookup_expr='name__iexact'
    )
    director_contains = filters.CharFilter(
        field_name="directors", lookup_expr='name__icontains'
    )
    writer = filters.CharFilter(
        field_name="writers", lookup_expr='name__iexact'
    )
    writer_contains = filters.CharFilter(
        field_name="writers", lookup_expr='name__icontains'
    )
    actor = filters.CharFilter(field_name="actors", lookup_expr='name__iexact')
    actor_contains = filters.CharFilter(
        field_name="actors", lookup_expr='name__icontains'
    )
    genre = filters.CharFilter(field_name="genres", lookup_expr='name__iexact')
    genre_contains = filters.CharFilter(
        field_name="genres", lookup_expr='name__icontains'
    )
    country = filters.CharFilter(
        field_name="countries", lookup_expr='name__iexact'
    )
    country_contains = filters.CharFilter(
        field_name="countries", lookup_expr='name__icontains'
    )
    lang = filters.CharFilter(
        field_name="languages", lookup_expr='name__iexact'
    )
    lang_contains = filters.CharFilter(
        field_name="languages", lookup_expr='name__icontains'
    )
    company = filters.CharFilter(
        field_name="company", lookup_expr='name__iexact'
    )
    company_contains = filters.CharFilter(
        field_name="company", lookup_expr='name__icontains'
    )
    rating = filters.CharFilter(
        field_name="rated",
        lookup_expr='name__iexact',
        label='Movie rating name',
    )
    rating_contains = filters.CharFilter(
        field_name="rated",
        lookup_expr='name__icontains',
        label='Movie rating contains',
    )
    sort_by = filters.CharFilter(
        method='filter_sort_by',
        label="Sort by a given value (title, -title, -imdb_score, etc.)",
    )

    def filter_sort_by(self, queryset, name, value):
        values = value.lower().split(',')
        return queryset.order_by(*values)

    class Meta:
        model = Movie
        fields = [
            'year',
            'min_year',
            'max_year',
            'imdb_score',
            'imdb_score_min',
            'imdb_score_max',
            'title',
            'title_contains',
            'genre',
            'genre_contains',
            'sort_by',
        ]