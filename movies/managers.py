"""Implementation of the movies managers.

This module is part of the OCMovies-API project and implements the managers
responsible to handle movies and their related data in the database.

"""

from django import db

from movies import models


class UniqueNameManager(db.models.Manager):
    """Generic manager responsible of handling entities described with a unique
    name."""

    def get_or_create_from_names(self, names):
        """Gets or creates objects from comma-separated names."""
        objects = []
        names = [name.strip() for name in names.split(',') if name.strip()]
        for name in names:
            obj, _ = self.get_or_create(name=name)
            objects.append(obj)
        return objects

    def get_by_natural_key(self, name):
        """Allows to use name as a natural key during fixture serialization."""
        return self.get(name=name)


class MovieManager(db.models.Manager):
    """Manager responsible of handling the collection of movies."""

    def create_movie(
        self,
        movie_info,
    ):
        """Loads and creates a new movie from info recovered from the csv
        file."""
        # Create related objects
        genres = models.Genre.objects.get_or_create_from_names(
            movie_info.pop('genres')
        )
        countries = models.Country.objects.get_or_create_from_names(
            movie_info.pop('countries')
        )
        languages = models.Language.objects.get_or_create_from_names(
            movie_info.pop('languages')
        )
        directors = models.Contributor.objects.get_or_create_from_names(
            movie_info.pop('directors')
        )
        writers = models.Contributor.objects.get_or_create_from_names(
            movie_info.pop('writers')
        )
        actors = models.Contributor.objects.get_or_create_from_names(
            movie_info.pop('actors')
        )
        production_company = models.Company.objects.get_or_create_from_names(
            movie_info.pop('production_company')
        )
        rating = models.Rating.objects.get_or_create_from_names(
            movie_info.pop('rated')
        )
        # Create the movie
        movie = self.create(
            **movie_info, company=production_company[0], rated=rating[0]
        )
        # Add the many to many relationships
        movie.add_genres(*genres)
        movie.add_directors(*directors)
        movie.add_writers(*writers)
        movie.add_actors(*actors)
        movie.add_countries(*countries)
        movie.add_languages(*languages)
