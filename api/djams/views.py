from django.shortcuts import render
from django.http.response import Http404
# from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, mixins, ViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics, filters

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

class SongList(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # serializer_class = SongSerializer

    # def get_queryset(self):
    #     name = self.kwargs['name']
    #     return Song.objects.filter(name=name)




