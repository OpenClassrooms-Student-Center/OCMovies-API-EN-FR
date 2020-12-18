from datetime import date
from decimal import Decimal
from unittest.mock import Mock

import pytest

from movies import normalizers as norm


class TestNormalizers:
    """Tests each individual normalizer function."""

    def test_transform_imdb_title_id_to_int_and_rename_to_id_renames_key(self):
        """Verifies that given the function
        transform_imdb_title_id_to_int_and_rename_to_id, if it recevies a
        dictionnary with a imdb_title_id key, it is renamed to id."""
        dic = {'imdb_title_id': 'tt00000001'}
        norm.transform_imdb_title_id_to_int_and_rename_to_id(dic)
        assert 'imdb_title_id' not in dic
        assert list(dic) == ['id']

    def test_transform_imdb_title_id_to_int_and_rename_to_id_converts_to_int(
        self,
    ):
        """Verifies that given a call to function
        transform_imdb_title_id_to_int_and_rename_to_id, when it recevied a
        dictionnary with a imdb_title_id key, the corresponding value is
        converted to an int."""
        dic = {'imdb_title_id': 'tt00000001'}
        norm.transform_imdb_title_id_to_int_and_rename_to_id(dic)
        assert isinstance(dic.get('id'), int)
        assert 'tt00000001'.endswith(str(dic.get('id')))

    def test_transform_year_to_int_converts_year_correctly(self):
        """Verifies that given a call to function transform_year_to_int, when
        if reveives a string ending with a 4-digits string, then the four
        digits are converted to int."""
        dic = {'year': 'aaaa    2018'}
        norm.transform_year_to_int(dic)
        assert isinstance(dic.get('year'), int)
        assert dic.get('year') == 2018

    def test_transform_date_published_to_python_date_converts_correctly(self):
        """Vertifies that given a call to function
        transform_date_published_to_python_date, when it receives an iso
        formated date as date, it is converted to a python date."""
        dic = {'date_published': '2020-12-01'}
        norm.transform_date_published_to_python_date(dic)
        assert isinstance(dic.get('date_published'), date)
        assert dic.get('date_published') == date(2020, 12, 1)

    def test_transform_date_published_to_python_date_converts_year_to_date(
        self,
    ):
        """Vertifies that given a call to function
        transform_date_published_to_python_date, when it receives an 4-digit
        year as a string, it is converted to the 1st January of that year."""
        dic = {'date_published': '2020'}
        norm.transform_date_published_to_python_date(dic)
        assert dic.get('date_published') == date(2020, 1, 1)

    def test_transform_date_published_to_python_date_raise_value_error(
        self,
    ):
        """Vertifies that given a call to function
        transform_date_published_to_python_date, when it receives an 2-digit
        year as a string, it is converted to the 1st January of that year."""
        dic = {'date_published': '20'}
        with pytest.raises(ValueError):
            norm.transform_date_published_to_python_date(dic)

    def test_transfrom_duration_into_integer_converts_to_int(self):
        dic = {'duration': '123'}
        norm.transfrom_duration_into_integer(dic)
        assert isinstance(dic.get('duration'), int)
        assert dic.get('duration') == 123

    @pytest.mark.parametrize(
        'field',
        [
            'countries',
            'genres',
            'languages',
            'directors',
            'writers',
            'production_company',
            'actors',
        ],
    )
    def test_transform_missing_fields_to_unkown_converts_empty_strings(
        self, field
    ):
        """Verifies than given a call to function
        transform_missing_fields_to_unkown, when if received a dictionnary
        entry with an empty string value, then value is set to 'Unknown'."""
        dic = {field: ''}
        norm.transform_missing_fields_to_unkown(dic)
        assert dic.get(field) == 'Unknown'

    @pytest.mark.parametrize(
        'field',
        [
            'countries',
            'genres',
            'languages',
            'directors',
            'writers',
            'production_company',
            'actors',
        ],
    )
    def test_transform_missing_fields_to_unkown_keeps_non_empty_strings(
        self, field
    ):
        """Verifies than given a call to function
        transform_missing_fields_to_unkown, when if received a dictionnary
        entry with an empty string value, then value is set to 'Unknown'."""
        dic = {field: 'aBc'}
        norm.transform_missing_fields_to_unkown(dic)
        assert dic.get(field) == 'aBc'

    def test_transform_missing_long_description_no_description_notice(self):
        # empty long_description
        dic = {'long_description': ''}
        norm.transform_missing_long_description_no_description_notice(dic)
        assert dic.get('long_description') == 'No long description provided'
        # non-empty long_description stay unmodified
        dic = {'long_description': 'aBc'}
        norm.transform_missing_long_description_no_description_notice(dic)
        assert dic.get('long_description') == 'aBc'

    def test_transform_avg_vote_to_decimal_converts_correctly(self):
        """Verifies that given a function call to
        transform_avg_vote_to_decimal, when it receives a string
        representing a decimal number, it is converted to a Decimal."""
        dic = {'avg_vote': '1.0'}
        norm.transform_avg_vote_to_decimal(dic)
        assert dic.get('avg_vote') == Decimal('1.0')

    def test_transform_imdb_score_to_decimal_converts_correctly(self):
        """Verifies that given a function call to
        transform_imdb_score_to_decimal, when it receives a string
        representing a real number, it is converted to a Decimal."""
        dic = {'imdb_score': '1.0'}
        norm.transform_imdb_score_to_decimal(dic)
        assert dic.get('imdb_score') == Decimal('1.0')

    @pytest.mark.parametrize(
        'metascore, result', [('10.0', Decimal('10.0')), ('', None)]
    )
    def test_transform_metascore_to_decimal_or_none_converts_correctly(
        self, metascore, result
    ):
        """Verifies that given a function call to
        transform_metascore_to_decimal_or_none, when it receives a string
        representing a real number, then it converts it to a Decimal.
        If an empty string is provided, the value is converted to None."""
        dic = {'metascore': metascore}
        norm.transform_metascore_to_decimal_or_none(dic)
        assert isinstance(dic.get('metascore'), type(result))
        assert dic.get('metascore') == result

    def test_transform_votes_to_integer_converts_correctly_to_int(self):
        """Verifies that given a function call to
        transform_votes_to_integer, when it receives a string
        representing an integer number, it converts it to the corresponding
        int."""
        dic = {'votes': '123'}
        norm.transform_votes_to_integer(dic)
        assert isinstance(dic.get('votes'), int)
        assert dic.get('votes') == 123

    @pytest.mark.parametrize(
        'value, budget, currency',
        [
            ('EUR 12345', 12345, 'EUR'),
            ('$ 12345', 12345, 'USD'),
            ('12345', 12345, 'USD'),
            ('$', None, None),
            ('', None, None),
            ('abcd 12345', None, None),
            ('abc 12345', 12345, 'ABC'),
        ],
    )
    def test_transform_budget_value_and_currency_or_none_extract_values(
        self, value, budget, currency
    ):
        """Verifies that given a function call to
        transform_budget_value_and_currency_or_none, when a string representing
        a currency and a budget are received, then it separates current and
        monetary amount."""
        dic = {'budget': value}
        norm.transform_budget_value_and_currency_or_none(dic)
        assert isinstance(dic.get('budget'), (int, type(None)))
        assert dic.get('budget') == budget
        assert dic.get('budget_currency') == currency

    @pytest.mark.parametrize(
        'key, value, result',
        [
            ('usa_gross_income', '$ 12345', 12345),
            ('usa_gross_income', '12345', 12345),
            ('usa_gross_income', 'abc', None),
            ('worldwide_gross_income', '$ 12345', 12345),
            ('worldwide_gross_income', '12345', 12345),
            ('worldwide_gross_income', 'abc', None),
            ('reviews_from_users', '12345', 12345),
            ('reviews_from_users', 'abc', None),
            ('reviews_from_critics', '12345', 12345),
            ('reviews_from_users', 'abc', None),
        ],
    )
    def test_transform_incomes_and_reviews_to_int_or_none_extract_values(
        self, key, value, result
    ):
        """Verifies that given a function call to
        transform_incomes_and_reviews_to_int_or_none, when it receives a string
        representing an income in USD, then it removes currency and converts
        monetary amount into int."""
        dic = {key: value}
        norm.transform_incomes_and_reviews_to_int_or_none(dic)
        assert isinstance(dic.get(key), (int, type(None)))
        assert dic.get(key) == result

    @pytest.mark.parametrize(
        'value, result',
        [
            ('abc', 'abc'),
            ('', 'Not rated or unkown rating'),
        ],
    )
    def test_transform_missing_rating_to_explicit_notice_works_correctly(
        self, value, result
    ):
        dic = {'rated': value}
        norm.transform_missing_rating_to_explicit_notice(dic)
        assert dic.get('rated') == result

    @pytest.mark.parametrize(
        'value, result',
        [
            ('abc', 'abc'),
            ('', None),
        ],
    )
    def test_transform_missing_rating_to_explicit_notice_works_correctly(
        self, value, result
    ):
        """Verifies that given a function call to
        transform_missing_rating_to_explicit_notice, when it receives a string
        representing the url of an image, then it does nothing. If the string
        is empty, then it is transformed to None"""
        dic = {'image_url': value}
        norm.transform_missing_image_to_none(dic)
        assert dic.get('image_url') == result


class TestMovieNormalizer:
    """Tests methods from the MovieNormalizer class."""

    @pytest.mark.parametrize(
        'movies',
        [range(0), range(1), range(10)],
    )
    def test_normalize_all_calls_normalize_as_expected(self, mocker, movies):
        """Verifies that given a list of movies sent to normalize_all,
        if the list is not empty, the nomalize is called the right number of
        times."""
        mock_normalize = mocker.patch(
            'movies.normalizers.MovieNormalizer.normalize'
        )
        movie_normalizer = norm.MovieNormalizer()
        movie_normalizer.normalize_all(movies)
        for i, _ in enumerate(movies):
            mock_normalize.assert_any_call(i)

    @pytest.mark.parametrize(
        'normalizers', [[Mock()], [Mock() for _ in range(10)]]
    )
    def test_normalize_call_all_normalizers(self, monkeypatch, normalizers):
        """Verifies that given normalize receives an object, if there are
        normalizers, then each normalizer is called with the object."""
        monkeypatch.setattr(
            'movies.normalizers.MovieNormalizer.normalizers', normalizers
        )
        movie_normalizer = norm.MovieNormalizer()
        movie_normalizer.normalize(1)
        for normalizer in normalizers:
            normalizer.assert_called_once_with(1)

    def test_all_normalizers_are_registered_to_movie_normalizer(self):
        """Verifies that given a tranform function is defined in the module,
        if it is public, then it is registered in the normalizers."""
        normalizers = [
            getattr(norm, elt)
            for elt in dir(norm)
            if elt.startswith('transform')
        ]
        for func in normalizers:
            assert func in norm.MovieNormalizer.normalizers