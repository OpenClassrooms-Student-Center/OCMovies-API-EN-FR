import pytest

from movies import models


@pytest.mark.django_db
class TestUniqueNameManager:
    """Integration tests on the UniqueNameManager methods."""

    def test_get_or_create_from_names_creates_one_contributor(self):
        models.Contributor.objects.get_or_create_from_names('Mathieu Nebra')
        assert models.Contributor.objects.count() == 1

    def test_get_or_create_from_names_gets_existing_contributor(self):
        models.Contributor.objects.create(name='Mathieu Nebra')
        models.Contributor.objects.get_or_create_from_names('Mathieu Nebra')
        assert models.Contributor.objects.count() == 1

    def test_get_or_create_from_names_creates_several_contributor(self):
        models.Contributor.objects.get_or_create_from_names(
            'Mathieu Nebra, Zozor'
        )
        assert models.Contributor.objects.count() == 2

    def test_get_or_create_from_names_creates_and_gets_several_contributor(
        self,
    ):
        models.Contributor.objects.create(name='Mathieu Nebra')
        models.Contributor.objects.get_or_create_from_names(
            'Mathieu Nebra, Zozor'
        )
        assert models.Contributor.objects.count() == 2

    def test_get_by_natural_key_returns_correct_object(self):
        result = models.Contributor.objects.get_or_create_from_names(
            'Mathieu Nebra'
        )
        assert (
            models.Contributor.objects.get_by_natural_key('Mathieu Nebra').id
            == result[0].id
        )
