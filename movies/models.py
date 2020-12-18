"""Implementation of the movies models.

This module is part of the OCMovies-API project and implements the models
responsible to describe the business object representing movies and their 
related data (country, language, contributors, etc.).

"""

from django.db import models
from django.urls import reverse

from . import managers


class Movie(models.Model):
    """Represent movie info as extracted from the IMDb database."""

    id = models.BigIntegerField('imdb title id', primary_key=True)
    title = models.CharField('movie title', max_length=255)
    original_title = models.CharField('original movie title', max_length=255)
    year = models.IntegerField('movie year')
    date_published = models.DateField('movie publishing date')
    duration = models.IntegerField('movie duration')
    description = models.TextField('movie short description', blank=True)
    long_description = models.TextField('movie long description', blank=True)
    avg_vote = models.DecimalField(
        'average user vote', max_digits=3, decimal_places=1
    )
    imdb_score = models.DecimalField(
        'movie imdb score', max_digits=3, decimal_places=1
    )
    metascore = models.DecimalField(
        'movie metascore', max_digits=5, decimal_places=1, null=True
    )
    votes = models.IntegerField('number of votes')
    budget = models.BigIntegerField('movie budget', null=True)
    budget_currency = models.CharField(
        'movie budget currency', max_length=5, null=True
    )
    usa_gross_income = models.BigIntegerField(
        'movie gross income in the usa', null=True
    )
    worldwide_gross_income = models.BigIntegerField(
        'movie gross income worldwide', null=True
    )
    reviews_from_users = models.IntegerField(
        'number of reviews from users', null=True
    )
    reviews_from_critics = models.IntegerField(
        'number of reviews from critics', null=True
    )
    image_url = models.URLField('poster image url', null=True)

    actors = models.ManyToManyField(
        'Contributor', through='MovieActor', related_name='movies_as_actor'
    )
    directors = models.ManyToManyField(
        'Contributor',
        through='MovieDirector',
        related_name='movies_as_director',
    )
    writers = models.ManyToManyField(
        'Contributor', through='MovieWriter', related_name='movies_as_writer'
    )
    genres = models.ManyToManyField('Genre', related_name='movies')
    countries = models.ManyToManyField('Country', related_name='movies')
    languages = models.ManyToManyField('Language', related_name='movies')
    rated = models.ForeignKey(
        'Rating', on_delete=models.SET_NULL, related_name='movies', null=True
    )
    company = models.ForeignKey(
        'Company', on_delete=models.SET_NULL, related_name='movies', null=True
    )

    objects = managers.MovieManager()

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'movies'

    def __str__(self):
        return f'{self.title} ({self.imdb_title_id})'

    @property
    def imdb_title_id(self):
        """Movie IMDB unique id."""
        return f"tt{self.id:07d}"

    @property
    def imdb_url(self):
        """URL of the movie on the IMDB website."""
        return f"https://www.imdb.com/title/{self.imdb_title_id}/"

    @property
    def usa_gross_income_currency(self):
        return 'USD'

    @property
    def worldwide_gross_income_currency(self):
        return 'USD'

    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'pk': self.id})

    def add_directors(self, *directors):
        """Adds one or several positioned directors to the current movie."""
        n_directors = self.directors.count()
        for position, director in enumerate(directors, start=n_directors + 1):
            self.directors.add(
                director, through_defaults={'position': position}
            )

    def add_actors(self, *actors):
        """Adds one or several positioned actors to the current movie."""
        n_actors = self.actors.count()
        for position, actor in enumerate(actors, start=n_actors + 1):
            self.actors.add(actor, through_defaults={'position': position})

    def add_writers(self, *writers):
        """Adds one or several positioned writers to the current movie."""
        n_writers = self.writers.count()
        for position, writer in enumerate(writers, start=n_writers + 1):
            self.writers.add(writer, through_defaults={'position': position})

    def add_genres(self, *genres):
        """Adds one or several genres to the current movie."""
        for genre in genres:
            self.genres.add(genre)

    def add_countries(self, *countries):
        """Adds one or several countries to the current movie."""
        for country in countries:
            self.countries.add(country)

    def add_languages(self, *languages):
        """Adds one or several languages to the current movie."""
        for language in languages:
            self.languages.add(language)


class Contributor(models.Model):
    """Represents a person having contributed to a movie either as actor,
    director or writer."""

    name = models.CharField(
        'contributor full name', max_length=200, unique=True
    )

    objects = managers.UniqueNameManager()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'contributors'

    def __str__(self):
        return self.name

    def natural_key(self):
        """Returns the natural key used for fixture serialization."""
        return self.name


class MovieDirector(models.Model):
    """Represents the association between a movie and its director(s)."""

    movie = models.ForeignKey(
        'Movie', on_delete=models.CASCADE, related_name="moviedirectors"
    )
    director = models.ForeignKey(
        'Contributor', on_delete=models.CASCADE, related_name="directormovies"
    )
    position = models.IntegerField('position in the directors list', null=True)

    class Meta:
        ordering = ['movie__id', 'position']
        verbose_name_plural = 'moviedirectors'

    def __str__(self):
        return f"{self.movie} - {self.director} ({self.position})"


class MovieActor(models.Model):
    """Represents the association between a movie and its actors(s)."""

    movie = models.ForeignKey(
        'Movie', on_delete=models.CASCADE, related_name="movieactors"
    )
    actor = models.ForeignKey(
        'Contributor', on_delete=models.CASCADE, related_name="movieactors"
    )
    position = models.IntegerField('position in the directors list', null=True)

    class Meta:
        ordering = ['movie__id', 'position']
        verbose_name_plural = 'movieactors'

    def __str__(self):
        return f"{self.movie} - {self.actor} ({self.position})"


class MovieWriter(models.Model):
    """Represents the association between a movie and its writer(s)."""

    movie = models.ForeignKey(
        'Movie', on_delete=models.CASCADE, related_name="moviewriters"
    )
    writer = models.ForeignKey(
        'Contributor', on_delete=models.CASCADE, related_name="writermovies"
    )
    position = models.IntegerField('position in the directors list', null=True)

    class Meta:
        ordering = ['movie__id', 'position']
        verbose_name_plural = 'moviewriters'

    def __str__(self):
        return f"{self.movie} - {self.writer} ({self.position})"


class Genre(models.Model):
    """Represents the genre of the movie."""

    name = models.CharField('genre of the movie', max_length=200, unique=True)

    objects = managers.UniqueNameManager()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'genres'

    def __str__(self):
        return self.name

    def natural_key(self):
        """Returns the natural key used for fixture serialization."""
        return self.name


class Country(models.Model):
    """Represents the country where a movie was created."""

    name = models.CharField('country name', max_length=200, unique=True)

    objects = managers.UniqueNameManager()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.name

    def natural_key(self):
        """Returns the natural key used for fixture serialization."""
        return self.name


class Language(models.Model):
    """Represents a language for a movie or its translation."""

    name = models.CharField('language name', max_length=200, unique=True)

    objects = managers.UniqueNameManager()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'languages'

    def __str__(self):
        return self.name

    def natural_key(self):
        """Returns the natural key used for fixture serialization."""
        return self.name


class Rating(models.Model):
    """Represents a rating attributed to a movie."""

    name = models.CharField('rating name', max_length=200, unique=True)

    objects = managers.UniqueNameManager()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'ratings'

    def __str__(self):
        return self.name

    def natural_key(self):
        """Returns the natural key used for fixture serialization."""
        return self.name


class Company(models.Model):
    """Represents a production company publishing a movie."""

    name = models.CharField(
        'production company name', max_length=200, unique=True
    )

    objects = managers.UniqueNameManager()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name

    def natural_key(self):
        """Returns the natural key used for fixture serialization."""
        return self.name
