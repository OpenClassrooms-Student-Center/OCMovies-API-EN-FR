"""Implementation of the create_db command.

This module is part of the OCMovies-API project and implement the create_db
command to restore the database from a sqlite3 backup file or from csv data.

"""

import csv
from io import TextIOWrapper
from pathlib import Path
from shutil import copyfile
from zipfile import ZipFile

from django.core.management import call_command
from django_tqdm import BaseCommand
from django.conf import settings

from movies.models import Movie
from movies.normalizers import MovieNormalizer


class Command(BaseCommand):
    """Implements the create_db cli command that creates a db from a file."""

    help = 'Creates the database with movies information'

    def add_arguments(self, parser):
        parser.add_argument(
            '--from-csv',
            action="store_true",
            default=False,
            dest='fromcsv',
            help='create db from raw data csv',
        )

    def handle(self, *args, **options):
        """Global entry point of the command, handles the cli options."""
        # if  database exists, a backup is done and actual db is removed
        dbname = settings.DATABASES['default']['NAME']
        dbname_bkp = Path(f'{dbname}.bkp')
        try:
            copyfile(
                dbname,
                dbname_bkp,
            )
            dbname.unlink()
        except FileNotFoundError:
            pass

        if options['fromcsv']:
            self.create_db_from_csv()
        else:
            self.create_db_default(dbname)

    def create_db_from_csv(self):
        """Main entry point of the --from-csv option."""
        normalizer = MovieNormalizer()

        self.stdout.write(
            self.style.MIGRATE_HEADING('Executing the migrations...')
        )
        call_command('migrate')

        self.stdout.write(
            self.style.MIGRATE_HEADING('Inserting the movies...')
        )
        with ZipFile('data/movies.csv.zip') as zf:
            with zf.open('movies.csv', 'r') as infile:
                reader = csv.DictReader(TextIOWrapper(infile, 'utf-8'))
                t = self.tqdm(total=85855)
                for i, movie_info in enumerate(reader, start=1):
                    t.update(1)
                    normalizer.normalize(movie_info)
                    Movie.objects.create_movie(movie_info)

    def create_db_default(self, dbname):
        """Main entry point of the default option using a db.sqlite3 backup."""
        self.stdout.write(
            self.style.MIGRATE_HEADING('Installation of the database')
        )
        self.stdout.write(
            'Populating database with movies info...', ending=' '
        )
        with ZipFile('data/movies.db.zip', 'r') as zipobj:
            zipobj.extractall(path=str(settings.BASE_DIR))
            Path(settings.BASE_DIR / 'db.sqlite3').replace(dbname)
        self.stdout.write(self.style.SUCCESS('OK'))