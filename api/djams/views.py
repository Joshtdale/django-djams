from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from .models import Song
from .serializers import SongSerializer
from rest_framework.response import Response

class SongAPIView(APIView):
    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404

    # READ
    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = SongSerializer(data)

        else: 
            data = Song.objects.all()
            serializer = SongSerializer(data, many=True)

        return Response(serializer.data)

    # Create
    def post(self, request, format=None):
        data = request.data
        serializer = SongSerializer(data=data)

        # validity check
        serializer.is_valid(raise_exception=True)

        # save
        serializer.save()

        # frontend result
        response = Response()

        response.data = {
            'message': 'Song Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        Song_update = Song.objects.get(pk=pk)
        data = request.data
        serializer = SongSerializer(instance=Song_update, data=data, partial=True)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()

        response.data = {
            'message': 'Song successfully updated',
            'data': serializer.data
        }

        return response