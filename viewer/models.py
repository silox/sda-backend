from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class Genre(models.Model):
    name = models.CharField(max_length=128)
    available_for_children = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}{"" if self.available_for_children else " (18+)"}'


class Movie(models.Model):
    title = models.CharField(max_length=128)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.IntegerField()
    released = models.DateField()
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    biography = models.TextField()
