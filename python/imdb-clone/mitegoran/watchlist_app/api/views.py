from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist_app.models import Media, StreamPlatform
from watchlist_app.api.serializers import MediaSerializer, StreamPlatformSerializer


class MediaListAV(APIView):
    def get(self, request):
        media_list = Media.objects.all()
        serializer = MediaSerializer(media_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MediaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MediaAV(APIView):
    def get(self, request, pk):
        try:
            media = Media.objects.get(pk=pk)
        except Media.DoesNotExist:
            return Response({'error': 'Media not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MediaSerializer(media)
        return Response(serializer.data)

    def put(self, request, pk):
        media = Media.objects.get(pk=pk)
        serializer = MediaSerializer(media, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        media = Media.objects.get(pk=pk)
        media.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatformListAV(APIView):
    def get(self, request):
        platform_list = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformAV(APIView):
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Stream platform not found'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
