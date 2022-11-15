from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

class Album(models.Model):
    title = models.CharField(max_length=30, null=False)

class Song(models.Model):
    title = models.CharField(max_length=30, null=False)
    duration = models.FloatField(null=True, blank=True)
    track_number = models.IntegerField(default=0, validators=[MinValueValidator(0)])