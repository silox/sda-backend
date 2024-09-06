from django.urls import path

from viewer.views import (
    MovieListView, MovieCreateView, GenreCreateView, MovieUpdateView, GenreUpdateView,
    MovieDeleteView, GenreDeleteView, MovieDetailView, GenreListView, GenreDetailView,
)

app_name = 'viewer'

urlpatterns = [
    path('movie/', MovieListView.as_view(), name='movie_list'),
    path('movie/detail/<pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('movie/create', MovieCreateView.as_view(), name='movie_create'),
    path('movie/update/<pk>', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/delete/<pk>', MovieDeleteView.as_view(), name='movie_delete'),

    path('genre/', GenreListView.as_view(), name='genre_list'),
    path('genre/detail/<pk>', GenreDetailView.as_view(), name='genre_detail'),
    path('genre/create/', GenreCreateView.as_view(), name='genre_create'),
    path('genre/update/<pk>', GenreUpdateView.as_view(), name='genre_update'),
    path('genre/delete/<pk>', GenreDeleteView.as_view(), name='genre_delete'),
]
