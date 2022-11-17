from rest_framework import serializers
from .models import *

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model= Genre
        fields = ('name',)

class ArtistSerializer(serializers.ModelSerializer):
    # song = SongSerializer()
    class Meta:
        model= Artist
        fields = "__all__"

    # def create(self, validated_data):
    #     artist = validated_data.pop('artist')
    #     art_instance = Artist.objects.get(name=artist['name'])
    #     song = Song.objects.create(**validated_data, artist=art_instance)
    #     return song


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model= Album
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    artist = ArtistSerializer(many=True)
    album = AlbumSerializer(many=True)
    class Meta:
        model = Song
        fields = (
            'name',
            'track_number',
            'artist',
            'album',
            'duration', 
            'genre'
            )

    def create(self, validated_data):
        genre = validated_data.pop('genre')
        artists = validated_data.pop('artist')
        # albums = validated_data.pop('album')

        gen_instance, created = Genre.objects.get_or_create(name=genre['name'])
        song = Song.objects.create(**validated_data, genre=gen_instance)
        
        for artist in artists:
            art_instance, created = Artist.objects.get_or_create(name=artist['name'])
            song.artist.add(art_instance)
        # for album in albums:
        #     alb_instance, created = Album.objects.get_or_create(name=album['name'])
        #     song.album.add(alb_instance)

        return song
        # return "Created successfully"
        # return { 
        #         "message": "Created successfully",
        #         "song": song
        #     }

