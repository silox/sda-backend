import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView, DetailView

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


class MovieDetailView(DetailView):
    template_name = 'movie_detail.html'
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


class MovieDeleteView(DeleteView):
    template_name = 'obj_delete_form.html'
    model = Movie
    success_url = reverse_lazy('index')
    extra_context = {'model_name': 'movie'}


class GenreCreateView(CreateView):
    template_name = 'obj_create_form.html'
    form_class = GenreForm
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        logger.warning('User provided invalid data.')
        return super().form_invalid(form)


class GenreUpdateView(UpdateView):
    template_name = 'obj_create_form.html'
    model = Genre
    form_class = GenreForm
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        logger.warning('User provided invalid data while updating a genre.')
        return super().form_invalid(form)


class GenreDeleteView(DeleteView):
    template_name = 'obj_delete_form.html'
    model = Genre
    success_url = reverse_lazy('index')
    extra_context = {'model_name': 'genre'}
