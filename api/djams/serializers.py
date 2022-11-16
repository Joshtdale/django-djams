from rest_framework import serializers
from .models import *

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model= Genre
        fields = ('name',)

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model= Artist
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model= Album
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    artist = ArtistSerializer(many=True)
    class Meta:
        model = Song
        fields = (
            'name',
            'track_number',
            'artist',
            'duration', 
            'genre'
            )

    def create(self, validated_data):
        genre = validated_data.pop('genre')
        gen_instance = Genre.objects.get(name=genre['name'])
        song = Song.objects.create(**validated_data, genre=gen_instance)
        return song

