import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, FormView, CreateView, UpdateView

from viewer.forms import MovieForm, GenreForm
from viewer.models import Movie, Genre

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
        context={'movies_url': reverse('movie_list')}
    )


class MovieListView(ListView):
    template_name = 'movie_list.html'
    model = Movie


class MovieCreateView(CreateView):
    template_name = 'obj_create_form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movie_list')

    def form_invalid(self, form):
        logger.warning('User provided invalid data.')
        return super().form_invalid(form)


class MovieUpdateView(UpdateView):
    template_name = 'obj_create_form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        logger.warning('User provided invalid data while updating a movie.')
        return super().form_invalid(form)


class GenreCreateView(FormView):
    template_name = 'obj_create_form.html'
    form_class = GenreForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Genre.objects.create(
            name=cleaned_data['name'],
            available_for_children=cleaned_data['available_for_children'],
        )
        return result

    def form_invalid(self, form):
        logger.warning('User provided invalid data.')
        return super().form_invalid(form)
