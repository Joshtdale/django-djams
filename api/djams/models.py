from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator


class Song(models.Model):
    name = models.CharField(max_length=30, null=False)
    duration = models.FloatField(null=True, blank=True)
    track_number = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT, null=True, blank=True)
    artist = models.ManyToManyField('Artist')
    album =  models.ManyToManyField('Album')
    # playlist = models.ManyToManyField('Playlist')

class Album(models.Model):
    name = models.CharField(max_length=30, null=False)
    artist = models.ManyToManyField('Artist')

class Artist(models.Model):
    name = models.CharField(max_length=30, null=False)

class Genre(models.Model):
    name = models.CharField(max_length=30, null=False)

class Playlist(models.Model):
    name = models.CharField(max_length=30, null=False)