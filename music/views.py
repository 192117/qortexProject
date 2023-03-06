from rest_framework import generics

from .models import Album, Artist, Song, Track
from .serializers import (AlbumCreateSerializer, AlbumListSerializer, ArtistCreateSerializer, ArtistListSerializer,
                          SongCreateSerializer, TrackCreateSerializer, TrackListSerializer)


class ArtistCreateView(generics.CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistCreateSerializer


class AlbumCreateView(generics.CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumCreateSerializer


class SongCreateView(generics.CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongCreateSerializer


class TrackCreateView(generics.CreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackCreateSerializer


class TrackListView(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackListSerializer


class AlbumListView(generics.ListAPIView):
    queryset = Album.objects.prefetch_related('tracks').all()
    serializer_class = AlbumListSerializer


class ArtistListView(generics.ListAPIView):
    queryset = Artist.objects.prefetch_related('album').all()
    serializer_class = ArtistListSerializer


class ArtistRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.prefetch_related('album').all()
    serializer_class = ArtistListSerializer


class AlbumRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.prefetch_related('tracks').all()
    serializer_class = AlbumListSerializer


class SongRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongCreateSerializer


class TrackRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackListSerializer
