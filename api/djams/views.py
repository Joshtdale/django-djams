from django.shortcuts import render
from django.http.response import Http404
# from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, mixins, ViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    http_method_names = ['get', 'post']

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    # http_method_names = ['get', 'post', 'put']

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

# class SongViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin):
#     serializer_class = SongSerializer
#     queryset = Song.objects.all()
    

class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    http_method_names = ['get', 'post']

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    http_method_names = ['get', 'post']

# class SongAPIView(APIView):
#     def get_object(self, pk):
#         try:
#             return Song.objects.get(pk=pk)
#         except Song.DoesNotExist:
#             raise Http404

#     # READ
#     def get(self, request, pk=None, format=None):
#         if pk:
#             data = self.get_object(pk)
#             serializer = SongSerializer(data)

#         else: 
#             data = Song.objects.all()
#             serializer = SongSerializer(data, many=True)

#         return Response(serializer.data)

#     # Create
#     def post(self, request, format=None):
#         data = request.data
#         serializer = SongSerializer(data=data)

#         # validity check
#         serializer.is_valid(raise_exception=True)

#         # save
#         serializer.save()

#         # frontend result
#         response = Response()

#         response.data = {
#             'message': 'Song Created Successfully',
#             'data': serializer.data
#         }

#         return response

    # def put(self, request, pk=None, format=None):
    #     Song_update = Song.objects.get(pk=pk)
    #     data = request.data
    #     serializer = SongSerializer(instance=Song_update, data=data, partial=True)
        
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     response = Response()

    #     response.data = {
    #         'message': 'Song successfully updated',
    #         'data': serializer.data
    #     }

    #     return response



