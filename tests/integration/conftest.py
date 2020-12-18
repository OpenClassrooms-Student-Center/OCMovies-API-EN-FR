from pytest_factoryboy import register

from movies import factories


register(factories.ContributorFactory)
register(factories.GenreFactory)
register(factories.CountryFactory)
register(factories.LanguageFactory)
register(factories.RatingFactory)
register(factories.CompanyFactory)
register(factories.MovieFactory)