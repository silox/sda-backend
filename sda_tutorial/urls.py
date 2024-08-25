"""
URL configuration for sda_tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from viewer.models import Genre, Movie
from viewer.views import (
    MovieListView, average_rating, hello, index, MovieCreateView, GenreCreateView, MovieUpdateView,
    GenreUpdateView, MovieDeleteView, GenreDeleteView
)

admin.site.register(Genre)
admin.site.register(Movie)

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('hello/<s0>', hello, name='hello'),
    path('movie/', MovieListView.as_view(), name='movie_list'),
    path('movie/create', MovieCreateView.as_view(), name='movie_create'),
    path('movie/update/<pk>', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/delete/<pk>', MovieDeleteView.as_view(), name='movie_delete'),
    path('movies/average-rating/', average_rating, name='average_rating'),
    path('genre/create/', GenreCreateView.as_view(), name='genre_create'),
    path('genre/update/<pk>', GenreUpdateView.as_view(), name='genre_update'),
    path('genre/delete/<pk>', GenreDeleteView.as_view(), name='genre_delete'),
]
