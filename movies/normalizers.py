"""Implementation of the normalizer object.

This module is part of the OCMovies-API project and implements a 
normalizer object whose responsibility is to clean the raw data before 
building the project database.

"""

from datetime import date
from decimal import Decimal
import re


def transform_imdb_title_id_to_int_and_rename_to_id(movie):
    imdb_title_id = movie.pop('imdb_title_id')
    movie['id'] = int(imdb_title_id.strip('tt'.lstrip('0')))


def transform_year_to_int(movie):
    movie['year'] = int(re.sub(r'\D', '', movie['year'].strip()))


def transform_date_published_to_python_date(movie):
    try:
        movie['date_published'] = date.fromisoformat(movie['date_published'])
    except ValueError:
        movie['date_published'] = date.fromisoformat(
            f"{movie['date_published']}-01-01"
        )


def transfrom_duration_into_integer(movie):
    movie['duration'] = int(movie['duration'])


def _transform_missing_item_to_unkown(movie, key):
    value = movie.get(key)
    movie[key] = (
        value if isinstance(value, str) and value.strip() else 'Unknown'
    )


def transform_missing_fields_to_unkown(movie):
    for key in (
        'countries',
        'genres',
        'languages',
        'directors',
        'writers',
        'production_company',
        'actors',
    ):
        _transform_missing_item_to_unkown(movie, key)


def transform_missing_long_description_no_description_notice(movie):
    value = movie.pop('long_description')
    movie['long_description'] = (
        value if value.strip() else 'No long description provided'
    )


def transform_avg_vote_to_decimal(movie):
    value = movie.pop('avg_vote', '').strip()
    movie['avg_vote'] = Decimal(value)


def transform_imdb_score_to_decimal(movie):
    value = movie.pop('imdb_score', '').strip()
    movie['imdb_score'] = Decimal(value)


def transform_metascore_to_decimal_or_none(movie):
    value = movie.pop('metascore', '').strip()
    movie['metascore'] = Decimal(value) if value else None


def transform_votes_to_integer(movie):
    value = movie.pop('votes')
    movie['votes'] = int(value)


def transform_budget_value_and_currency_or_none(movie):
    budget = movie.pop('budget', '').replace('$', 'USD').upper()
    match = re.match(r'(?P<currency>\D{3})\s+(?P<value>\d+)', budget)
    if not match:
        match = re.match(
            r'(?P<currency>\S+)\s+(?P<value>\d+)', f'USD {budget}'
        )
    movie['budget'] = int(match.group('value')) if match else None
    movie['budget_currency'] = match.group('currency') if match else None


def transform_incomes_and_reviews_to_int_or_none(movie):
    for key in (
        'usa_gross_income',
        'worldwide_gross_income',
        'reviews_from_users',
        'reviews_from_critics',
    ):
        values = re.findall(r'\d+', movie.pop(key, ''))
        movie[key] = int(values[0]) if values else None


def transform_missing_rating_to_explicit_notice(movie):
    value = movie.pop('rated', '').strip()
    movie['rated'] = value or 'Not rated or unkown rating'


def transform_missing_image_to_none(movie):
    value = movie.pop('image_url').strip()
    movie['image_url'] = value or None


class MovieNormalizer:
    """Object normalizing movie information before insertion into database."""

    normalizers = [
        transform_imdb_title_id_to_int_and_rename_to_id,
        transform_year_to_int,
        transform_date_published_to_python_date,
        transfrom_duration_into_integer,
        transform_missing_fields_to_unkown,
        transform_missing_long_description_no_description_notice,
        transform_avg_vote_to_decimal,
        transform_imdb_score_to_decimal,
        transform_metascore_to_decimal_or_none,
        transform_votes_to_integer,
        transform_budget_value_and_currency_or_none,
        transform_incomes_and_reviews_to_int_or_none,
        transform_missing_rating_to_explicit_notice,
        transform_missing_image_to_none,
    ]

    def normalize(self, product):
        """Normalizes an individual movie."""
        for normalizer in self.normalizers:
            normalizer(product)

    def normalize_all(self, movies):
        """Normalizes each movie present in the provided list of movies."""
        for movie in movies:
            self.normalize(movie)