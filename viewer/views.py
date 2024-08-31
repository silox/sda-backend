import logging

from django.shortcuts import render
from django.urls import reverse, reverse_lazy
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
        }
    )


class MovieListView(ListView):
    template_name = 'movie_list.html'
    model = Movie

    def get_context_data(self, **kwargs):
        movies = Movie.objects.all()
        return {
            **super().get_context_data(**kwargs),
            'average_rating': f'{sum(movie.rating for movie in movies) / len(movies):.2f}'
        }


class MovieDetailView(DetailView):
    template_name = 'movie_detail.html'
    model = Movie


class MovieCreateView(CreateView):
    template_name = 'movie_form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movie_list')

    def form_invalid(self, form):
        logger.warning('User provided invalid data.')
        return super().form_invalid(form)


class MovieUpdateView(UpdateView):
    template_name = 'movie_form.html'
    model = Movie
    form_class = MovieForm

    def form_invalid(self, form):
        logger.warning('User provided invalid data while updating a movie.')
        return super().form_invalid(form)

    def get_success_url(self):
        if '_continue' in self.request.POST:
            return reverse_lazy('movie_update', kwargs={'pk': self.object.pk})
        elif '_save' in self.request.POST:
            return reverse_lazy('movie_list')

        assert False, 'Unexpectedly got no _save or _continue in request.POST'


class MovieDeleteView(DeleteView):
    template_name = 'obj_delete_form.html'
    model = Movie
    success_url = reverse_lazy('movie_list')
    extra_context = {'model_name': 'movie'}


class GenreListView(ListView):
    template_name = 'genre_list.html'
    model = Genre


class GenreDetailView(DetailView):
    template_name = 'genre_detail.html'
    model = Genre


class GenreCreateView(CreateView):
    template_name = 'genre_form.html'
    form_class = GenreForm
    success_url = reverse_lazy('genre_list')

    def form_invalid(self, form):
        logger.warning('User provided invalid data.')
        return super().form_invalid(form)


class GenreUpdateView(UpdateView):
    template_name = 'genre_form.html'
    model = Genre
    form_class = GenreForm

    def form_invalid(self, form):
        logger.warning('User provided invalid data while updating a genre.')
        return super().form_invalid(form)

    def get_success_url(self):
        if '_continue' in self.request.POST:
            return reverse_lazy('genre_update', kwargs={'pk': self.object.pk})
        elif '_save' in self.request.POST:
            return reverse_lazy('genre_list')

        assert False, 'Unexpectedly got no _save or _continue in request.POST'


class GenreDeleteView(DeleteView):
    template_name = 'obj_delete_form.html'
    model = Genre
    success_url = reverse_lazy('genre_list')
    extra_context = {'model_name': 'genre'}
