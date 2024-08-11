# Task
# Vymaz duplicitne filmy (rovnaky nazov)

from django.core.management.base import BaseCommand

from viewer.models import Movie


class Command(BaseCommand):
    help = "Load movies from data/movies.csv"

    def handle(self, *args, **options):
        movie_titles = Movie.objects.values_list('title', flat=True)
        deleted_count = 0
        for title in movie_titles:
            movies_with_same_title = Movie.objects.filter(title=title)
            deleted_count += movies_with_same_title.count() - 1
            for movie in movies_with_same_title[1:]:
                movie.delete()

        print(f"Deleted {deleted_count} movies")
