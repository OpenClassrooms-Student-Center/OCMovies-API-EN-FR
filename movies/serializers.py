from rest_framework import serializers

from . import models


class GenreSerializer(serializers.ModelSerializer):
    """Serializer for the list of genre."""

    class Meta:
        model = models.Genre
        fields = ['id', 'name']


class MovieListSerializer(serializers.ModelSerializer):
    """Serializer for the list of movies."""

    directors = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)
    writers = serializers.StringRelatedField(many=True)
    genres = serializers.StringRelatedField(many=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='movie-detail', format='html', lookup_field='pk'
    )

    class Meta:
        model = models.Movie
        fields = [
            'id',
            'url',
            'imdb_url',
            'title',
            'year',
            'imdb_score',
            'votes',
            'image_url',
            'directors',
            'actors',
            'writers',
            'genres',
        ]


class MovieDetailSerializer(serializers.ModelSerializer):
    """Serializer for the list of movies."""

    directors = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)
    writers = serializers.StringRelatedField(many=True)
    genres = serializers.StringRelatedField(many=True)
    countries = serializers.StringRelatedField(many=True)
    languages = serializers.StringRelatedField(many=True)
    rated = serializers.StringRelatedField()
    company = serializers.StringRelatedField()

    class Meta:
        model = models.Movie
        fields = [
            'id',
            'url',
            'title',
            'original_title',
            'year',
            'date_published',
            'duration',
            'description',
            'long_description',
            'avg_vote',
            'imdb_score',
            'votes',
            'metascore',
            'budget',
            'budget_currency',
            'usa_gross_income',
            'worldwide_gross_income',
            'reviews_from_users',
            'reviews_from_critics',
            'image_url',
            'actors',
            'directors',
            'writers',
            'genres',
            'countries',
            'languages',
            'rated',
            'company',
        ]
