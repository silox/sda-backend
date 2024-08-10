from django.http import HttpResponse

from viewer.models import Movie


def movies(request):
    movies = Movie.objects.all()
    return HttpResponse(
        '\n'.join(movie.title for movie in movies),
        content_type='text/plain'
    )


def movie_detail(request, pk):
    return HttpResponse(
        pk,
        content_type='text/plain'
    )


def average_rating(request):
    return HttpResponse(
        f'Average rating: TODO',
        content_type='text/plain'
    )
