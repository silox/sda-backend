from datetime import date, timedelta
import logging

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from viewer.forms import MovieForm, GenreForm
from viewer.models import Movie, Genre

logger = logging.getLogger(__name__)


def hello(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request, template_name='hello.html',
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
    )


def index(request):
    movie = Movie.objects.filter(pk=request.GET.get('pk')).first()
    code = '' if movie is None else movie.description
    return render(
        request, template_name='index.html',
        context={
            'list_data': [0, 1, 2, 3],
            'dict_data': {'a': 1, 'b': 2, 'c': 3},
            'names': ['John', 'Peter', 'James'],
            'my_html_code': code,
            'br_test': 'text\n which contains\n multiple\nlines!',
            'my_test_date': date.today().replace(),
        }
    )


class MovieListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'movie_list.html'
    model = Movie
    permission_required = 'viewer.view_movie'

    def get_context_data(self, **kwargs):
        movies = Movie.objects.all()
        return {
            **super().get_context_data(**kwargs),
            'average_rating': f'{sum(movie.rating for movie in movies) / len(movies):.2f}'
        }


class MovieDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'movie_detail.html'
    model = Movie
    permission_required = 'viewer.view_movie'


class MovieCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'movie_form.html'
    form_class = MovieForm
    success_url = reverse_lazy('viewer:movie_list')
    permission_required = 'viewer.add_movie'

    def form_invalid(self, form):
        logger.warning('User provided invalid data.')
        return super().form_invalid(form)


class MovieUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'movie_form.html'
    model = Movie
    form_class = MovieForm
    permission_required = 'viewer.change_movie'

    def form_invalid(self, form):
        logger.warning('User provided invalid data while updating a movie.')
        return super().form_invalid(form)

    def get_success_url(self):
        if '_continue' in self.request.POST:
            return reverse_lazy('viewer:movie_update', kwargs={'pk': self.object.pk})
        elif '_save' in self.request.POST:
            return reverse_lazy('viewer:movie_list')

        assert False, 'Unexpectedly got no _save or _continue in request.POST'


class MovieDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'obj_delete_form.html'
    model = Movie
    success_url = reverse_lazy('viewer:movie_list')
    extra_context = {'model_name': 'movie'}
    permission_required = 'viewer.delete_movie'


class GenreListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'genre_list.html'
    model = Genre
    permission_required = 'viewer.view_genre'


class GenreDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'genre_detail.html'
    model = Genre
    permission_required = 'viewer.view_genre'


class GenreCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'genre_form.html'
    form_class = GenreForm
    success_url = reverse_lazy('viewer:genre_list')
    permission_required = 'viewer.add_genre'

    def form_invalid(self, form):
        logger.warning('User provided invalid data.')
        return super().form_invalid(form)


class GenreUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'genre_form.html'
    model = Genre
    form_class = GenreForm
    permission_required = 'viewer.change_genre'

    def form_invalid(self, form):
        logger.warning('User provided invalid data while updating a genre.')
        return super().form_invalid(form)

    def get_success_url(self):
        if '_continue' in self.request.POST:
            return reverse_lazy('viewer:genre_update', kwargs={'pk': self.object.pk})
        elif '_save' in self.request.POST:
            return reverse_lazy('viewer:genre_list')

        assert False, 'Unexpectedly got no _save or _continue in request.POST'


class GenreDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'obj_delete_form.html'
    model = Genre
    success_url = reverse_lazy('viewer:genre_list')
    extra_context = {'model_name': 'genre'}
    permission_required = 'viewer.delete_genre'
