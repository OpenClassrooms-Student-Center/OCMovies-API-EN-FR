import pytest

from movies import managers


class TestUniqueNameManager:
    """Tests methods from the UniqueNameManager."""

    def test_get_or_create_from_names_works_with_one_name(self, mocker):
        """Verifies get_or_create_from_names supports receiving one name."""
        mock = mocker.patch(
            'movies.managers.UniqueNameManager.get_or_create',
            return_value=("name_object", False),
        )
        manager = managers.UniqueNameManager()
        results = manager.get_or_create_from_names('name1')
        assert len(results) == 1
        assert results[0] == "name_object"
        mock.assert_called_once_with(name='name1')

    def test_get_or_create_from_names_behaves_correctly_if_no_name(
        self, mocker
    ):
        """Verifies there is no problem if the get_or_create_from_names method
        received an empty string."""
        mock = mocker.patch(
            'movies.managers.UniqueNameManager.get_or_create',
        )
        manager = managers.UniqueNameManager()
        results = manager.get_or_create_from_names('')
        assert len(results) == 0
        mock.assert_not_called()

    @pytest.mark.parametrize(
        'names, expected_results',
        [
            ('name1,name2', ['name1', 'name2']),
            ('name1, name2', ['name1', 'name2']),
            ('name1,  name2', ['name1', 'name2']),
        ],
    )
    def test_get_or_create_from_names_splits_names_correctly(
        self, mocker, names, expected_results
    ):
        """Verifies get_or_create_from_names work as expected whatever the
        number of spaces between names."""
        mock = mocker.patch(
            'movies.managers.UniqueNameManager.get_or_create',
            side_effect=[
                (f"{name}_object", False) for name in expected_results
            ],
        )
        manager = managers.UniqueNameManager()
        results = manager.get_or_create_from_names(names)
        assert results == [f"{name}_object" for name in expected_results]


class TestMovieManager:
    pass