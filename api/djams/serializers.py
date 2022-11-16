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
        # print(genre)
        artists = validated_data.pop('artist')
        
        

        # loop over artist and perform 
        # art_instance = Artist.objects.get(name=artist['name'])
        # song.artist.add(art_instance)



        # if genre:
        gen_instance, created = Genre.objects.get_or_create(name=genre['name'])
        song = Song.objects.create(**validated_data, genre=gen_instance)
        for artist in artists:
            art_instance, created = Artist.objects.get_or_create(name=artist['name'])
            song.artist.add(art_instance)
        # art_instance, created = Artist.objects.get_or_create(name=artist['name'])
        # song.artist.add(art_instance)
            # return song
        # elif artist:
        # artist = validated_data.pop('artist')
        # song2 = Song.objects.create(**validated_data, artist=art_instance)
        return song

