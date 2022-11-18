from rest_framework import serializers
from .models import *

class GenreField(serializers.RelatedField):
    def to_internal_value(self, data):
        obj, created = Genre.objects.get_or_create(**data)
        return obj
    def to_representation(self, value):
        return {
            "name": value.name
        }

class ArtistField(serializers.RelatedField):
    def to_internal_value(self, data):
        obj, created = Artist.objects.get_or_create(**data)
        return obj
    def to_representation(self, value):
        return {
            "name": value.name
        }

class AlbumField(serializers.RelatedField):
    def to_internal_value(self, data):
        obj, created = Album.objects.get_or_create(**data)
        return obj
    def to_representation(self, value):
        return {
            "name": value.name
        }