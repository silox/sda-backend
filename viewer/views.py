from django.http import HttpResponse

from viewer.models import Movie
from django.shortcuts import get_object_or_404


def movies(request):
    movies = Movie.objects.all()
    return HttpResponse(
        '\n'.join(movie.title for movie in movies),
        content_type='text/plain'
    )


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return HttpResponse(
        f'{movie.title}, {movie.genre}, {movie.rating}',
        content_type='text/plain'
    )


def average_rating(request):
    movies = Movie.objects.all()
    return HttpResponse(
        f'Average rating: {sum(movie.rating for movie in movies) / len(movies)}',
        content_type='text/plain'
    )
