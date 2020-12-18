"""Registration of the movies app models for their management through the 
admin interface."""

from django.contrib import admin

from . import models

# Registration of models for their administration through
# the admin interface
admin.site.register(models.Movie)
admin.site.register(models.MovieDirector)
admin.site.register(models.MovieActor)
admin.site.register(models.MovieWriter)
admin.site.register(models.Contributor)
admin.site.register(models.Genre)
admin.site.register(models.Country)
admin.site.register(models.Language)
admin.site.register(models.Rating)
admin.site.register(models.Company)