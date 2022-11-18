from rest_framework import serializers
from .models import *
from .fields import GenreField, ArtistField

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model= Genre
        fields = ('name',)

# class ArtistField(serializers.RelatedField):
# **data

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
    # genre = GenreSerializer()
    # artist = ArtistSerializer(many=True)
    album = AlbumSerializer(many=True)
    genre = GenreField(queryset=Genre.objects.all())
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

    # def create(self, validated_data):
    #     genre = validated_data.pop('genre')
    #     artists = validated_data.pop('artist')
    #     albums = validated_data.pop('album')

    #     gen_instance, created = Genre.objects.get_or_create(name=genre['name'])
    #     song = Song.objects.create(**validated_data, genre=gen_instance)

    #     for artist in artists:
    #         art_instance, created = Artist.objects.get_or_create(name=artist['name'])
    #         song.artist.add(art_instance)
    #     for album in albums:
    #         alb_instance, created = Album.objects.get_or_create(name=album['name'])
    #         song.album.add(alb_instance)

    #     return song
        # return "Created successfully"
        # return { 
        #         "message": "Created successfully",
        #         "song": song
        #     }

    # def update(self, instance, validated_data):
    #     genre_data = validated_data.pop('genre')
    #     artists_data = validated_data.pop('artist')
    #     # albums_data = validated_data.pop('album_musician')
    #     artists = (instance.artist).all()
    #     artists = list(artists)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.track_number = validated_data.get('track_number', instance.track_number)
    #     instance.artist = validated_data.get('artist', instance.artist)
    #     instance.save()

        # for artist_data in artists_data:
        #     artist = artists.pop(0)
        #     artist.name = artist_data.get('name', artist.name)
            # artist.release_date = artist_data.get('release_date', artist.release_date)
            # artist.num_stars = artist_data.get('num_stars', artist.num_stars)
        #     artist.set()
        # return instance

    # class Album(models.Model):
        # artist = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='album_musician', null=True, blank=True)
        # name = models.CharField(max_length=100)
        # release_date = models.DateField()
        # num_stars = models.IntegerField()
