import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

from viewer.forms import MovieForm, GenreForm, CustomAuthenticationForm, CustomPasswordChangeForm, SignUpForm
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


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        return {**super().get_context_data(), 'object': self.request.user}


class MovieListView(LoginRequiredMixin, ListView):
    template_name = 'movie_list.html'
    model = Movie

    def get_context_data(self, **kwargs):
        movies = Movie.objects.all()
        return {
            **super().get_context_data(**kwargs),
            'average_rating': f'{sum(movie.rating for movie in movies) / len(movies):.2f}'
        }


class MovieDetailView(LoginRequiredMixin, DetailView):
    template_name = 'movie_detail.html'
    model = Movie


class MovieCreateView(LoginRequiredMixin, CreateView):
    template_name = 'movie_form.html'
    form_class = MovieForm
    success_url = reverse_lazy('viewer:movie_list')

    def form_invalid(self, form):
        logger.warning('User provided invalid data.')
        return super().form_invalid(form)


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'movie_form.html'
    model = Movie
    form_class = MovieForm

    def form_invalid(self, form):
        logger.warning('User provided invalid data while updating a movie.')
        return super().form_invalid(form)

    def get_success_url(self):
        if '_continue' in self.request.POST:
            return reverse_lazy('viewer:movie_update', kwargs={'pk': self.object.pk})
        elif '_save' in self.request.POST:
            return reverse_lazy('viewer:movie_list')

        assert False, 'Unexpectedly got no _save or _continue in request.POST'


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'obj_delete_form.html'
    model = Movie
    success_url = reverse_lazy('viewer:movie_list')
    extra_context = {'model_name': 'movie'}


class GenreListView(LoginRequiredMixin, ListView):
    template_name = 'genre_list.html'
    model = Genre


class GenreDetailView(LoginRequiredMixin, DetailView):
    template_name = 'genre_detail.html'
    model = Genre


class GenreCreateView(LoginRequiredMixin, CreateView):
    template_name = 'genre_form.html'
    form_class = GenreForm
    success_url = reverse_lazy('viewer:genre_list')

    def form_invalid(self, form):
        logger.warning('User provided invalid data.')
        return super().form_invalid(form)


class GenreUpdateView(LoginRequiredMixin, UpdateView):
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
            return reverse_lazy('viewer:genre_list')

        assert False, 'Unexpectedly got no _save or _continue in request.POST'


class GenreDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'obj_delete_form.html'
    model = Genre
    success_url = reverse_lazy('viewer:genre_list')
    extra_context = {'model_name': 'genre'}


class SubmittableLoginView(LoginView):
    template_name = 'login_form.html'
    form_class = CustomAuthenticationForm
    next_page = reverse_lazy('index')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')


class SubmittablePasswordChangeView(PasswordChangeView):
    template_name = 'password_change_form.html'
    success_url = reverse_lazy('index')
    form_class = CustomPasswordChangeForm


class SignUpView(CreateView):
    template_name = 'sign_up_form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')
