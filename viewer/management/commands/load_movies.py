# Task
# Nacitaj filmy z data/movies.csv do db.

import csv
from datetime import date

from django.core.management.base import BaseCommand

from viewer.models import Genre, Movie


class Command(BaseCommand):
    help = "Load movies from data/movies.csv"

    def handle(self, *args, **options):
        with open('data/movies.csv') as file:
            csv_reader = csv.reader(file, delimiter=',')
            for line_num, row in enumerate(csv_reader):
                if line_num == 0:
                    continue

                title, genre, rating, released, description = row
                genre_obj, _ = Genre.objects.get_or_create(name=genre)

                Movie.objects.create(
                    title=title,
                    genre=genre_obj,
                    rating=int(float(rating)),
                    released=date(int(released), 1, 1),
                    description=description
                )

            print(f'Created movies: {line_num}')
