"""Implementation of the movies factories.

This module is part of the OCMovies-API project and implements the factories
usable as helpers to build easily model instances during tests.

"""

import datetime
from decimal import Decimal

import factory
from faker import Factory as FakerFactory

from . import models

fake = FakerFactory.create()


def _get_related(related_model, related_factory, number=3, total=None):
    """Handles extracted arguments for related instances."""
    count = related_model.objects.count()
    total = 2 * number if total is None else max(number, total)
    if count < total:
        for _ in range(total - count):
            related_factory()
    return related_model.objects.order_by('?')[:number]


class ContributorFactory(factory.django.DjangoModelFactory):
    """Factory responsible for building fake contributors for test purpose."""

    class Meta:
        model = models.Contributor

    name = factory.Faker('name')


class GenreFactory(factory.django.DjangoModelFactory):
    """Factory responsible fro building fake genre for test purpose."""

    class Meta:
        model = models.Genre

    name = factory.Iterator(
        [
            'History',
            'Drama',
            'Documentary',
            'Sport',
            'Music',
            'Animation',
            'News',
            'Adventure',
            'Adult',
            'Sci-Fi',
            'Family',
            'Romance',
            'Horror',
            'Comedy',
            'Biography',
            'Fantasy',
            'Film-Noir',
            'Crime',
            'Action',
            'Thriller',
            'Western',
            'Mystery',
            'Reality-TV',
            'War',
            'Musical',
        ]
    )


class CountryFactory(factory.django.DjangoModelFactory):
    """Factory responsible for building fake countries objects."""

    class Meta:
        model = models.Country

    name = factory.Faker('country')


class LanguageFactory(factory.django.DjangoModelFactory):
    """Factory responsible for building fake language objects."""

    class Meta:
        model = models.Language

    name = factory.Faker('language_name')


class RatingFactory(factory.django.DjangoModelFactory):
    """Factory responsible for building fake rating objects for test purpose."""

    class Meta:
        model = models.Rating

    name = factory.Sequence(lambda n: f"Rating-{n+1}")


class CompanyFactory(factory.django.DjangoModelFactory):
    """Factory responsible for building fake production company values for test purpose."""

    class Meta:
        model = models.Rating

    name = factory.Sequence(lambda n: f'Movie Company #{n+1}')


class MovieFactory(factory.django.DjangoModelFactory):
    """Factory responsible for building fake movies for test purpose."""

    class Meta:
        model = models.Movie

    id = factory.Faker('random_int', min=1, max=1000000)
    title = factory.LazyAttribute(
        lambda obj: fake.text(max_nb_chars=20).strip('.')
    )
    original_title = factory.LazyAttribute(lambda obj: obj.title)
    year = factory.Faker('random_int', min=1970, max=2020)
    date_published = factory.Faker(
        'date_between_dates',
        date_start=datetime.date(1950, 1, 1),
        date_end=datetime.date(2020, 12, 1),
    )
    duration = factory.Faker('random_int', min=1, max=150)
    description = factory.Faker('text')
    long_description = factory.Faker('text', max_nb_chars=300)
    avg_vote = factory.LazyAttribute(
        lambda obj: obj.imdb_score - Decimal('0.1')
    )
    imdb_score = factory.Faker(
        'pydecimal', min_value=1, max_value=10, right_digits=1
    )
    metascore = factory.Faker(
        'pydecimal', min_value=1, max_value=100, right_digits=1
    )
    votes = factory.Faker('random_int', min=100, max=10000)
    budget = factory.Faker('random_int', min=10000, max=10000000)
    budget_currency = 'USD'
    usa_gross_income = factory.Faker('random_int', min=10000, max=10000000)
    worldwide_gross_income = factory.Faker(
        'random_int', min=10000, max=10000000
    )
    reviews_from_users = factory.Faker('random_int', min=10, max=1000)
    reviews_from_critics = factory.Faker('random_int', min=10, max=1000)
    image_url = factory.Faker('image_url')

    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        """Post generation method to add genres to the created movie."""
        if not create:
            return  # add only where strategy is create

        genres_ = _get_related(models.Genre, GenreFactory)
        self.add_genres(*genres_)

    @factory.post_generation
    def countries(self, create, extracted, **kwargs):
        """Post generation method to add countries to the created movie."""
        if not create:
            return  # add only where strategy is create

        countries_ = _get_related(models.Country, CountryFactory)
        self.add_countries(*countries_)

    @factory.post_generation
    def languages(self, create, extracted, **kwargs):
        """Post generation method to add languages to the created movie."""
        if not create:
            return  # add only where strategy is create

        languages_ = _get_related(models.Language, LanguageFactory)
        self.add_languages(*languages_)

    @factory.post_generation
    def directors(self, create, extracted, **kwargs):
        """Post generation method to add directors to the created movie."""
        if not create:
            return  # add only where strategy is create

        directors_ = _get_related(
            models.Contributor, ContributorFactory, number=2, total=15
        )
        self.add_directors(*directors_)

    @factory.post_generation
    def writers(self, create, extracted, **kwargs):
        """Post generation method to add writers to the created movie."""
        if not create:
            return  # add only where strategy is create

        writers_ = _get_related(
            models.Contributor, ContributorFactory, number=2, total=15
        )
        self.add_writers(*writers_)

    @factory.post_generation
    def actors(self, create, extracted, **kwargs):
        """Post generation method to add actors to the created movie."""
        if not create:
            return  # add langages only where strategy is create

        actors_ = _get_related(
            models.Contributor, ContributorFactory, number=3, total=20
        )
        self.add_actors(*actors_)
