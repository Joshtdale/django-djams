from rest_framework import serializers
from .models import *
from .fields import *

class GenreSerializer(serializers.ModelSerializer):
    # album = AlbumField(many=True, queryset=Album.objects.all())
    # artist = ArtistField(many=True, queryset=Artist.objects.all())
    class Meta:
        model= Genre
        fields = ('name',)


class ArtistSerializer(serializers.ModelSerializer):
    # genre = GenreField(queryset=Genre.objects.all())
    # album = AlbumField(many=True, queryset=Album.objects.all())
    # song
    class Meta:
        model= Artist
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    # genre = GenreField(queryset=Genre.objects.all())
    artist = ArtistField(many=True, queryset=Artist.objects.all())
    class Meta:
        model= Album
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    genre = GenreField(queryset=Genre.objects.all())
    album = AlbumField(many=True, queryset=Album.objects.all())
    artist = ArtistField(many=True, queryset=Artist.objects.all())
    class Meta:
        model = Song
        fields = (
            'id',
            'name',
            'track_number',
            'artist',
            'album',
            'duration', 
            'genre'
            )

