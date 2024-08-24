import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, FormView

from viewer.forms import MovieForm
from viewer.models import Movie


logger = logging.getLogger(__name__)


def average_rating(request):
    movies = Movie.objects.all()
    return HttpResponse(
        f'Average rating: {sum(movie.rating for movie in movies) / len(movies)}',
        content_type='text/plain'
    )


def hello(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request, template_name='hello.html',
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
    )


def index(request):
    return render(
        request, template_name='index.html',
        context={'movies_url': reverse('movies')}
    )


class MoviesView(ListView):
    template_name = 'movies.html'
    model = Movie


class MovieCreateView(FormView):
    template_name = 'movie_create_form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movies')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Movie.objects.create(
            title=cleaned_data['title'],
            genre=cleaned_data['genre'],
            rating=cleaned_data['rating'],
            released=cleaned_data['released'],
            description=cleaned_data['description']
        )
        return result

    def form_invalid(self, form):
        logger.warning('User provided invalid data.')
        return super().form_invalid(form)
