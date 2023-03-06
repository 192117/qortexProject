from rest_framework import serializers

from .models import Album, Artist, Song, Track


class ArtistCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('name',)


class AlbumCreateSerializer(serializers.ModelSerializer):

    artist = serializers.SlugRelatedField(queryset=Artist.objects.all(), slug_field='name')

    class Meta:
        model = Album
        fields = ('name', 'artist', 'year',)


class TrackCreateSerializer(serializers.ModelSerializer):

    song = serializers.SlugRelatedField(queryset=Song.objects.all(), slug_field='name')
    album = serializers.SlugRelatedField(queryset=Album.objects.all(), slug_field='name')

    class Meta:
        model = Track
        fields = ('song', 'album', 'track_number',)


class SongCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('name',)


class TrackListSerializer(serializers.ModelSerializer):

    song = serializers.CharField(source='song.name')
    album = serializers.CharField(source='album.name')

    class Meta:
        model = Track
        fields = ('song', 'track_number', 'album')


class AlbumListSerializer(serializers.ModelSerializer):

    tracks = TrackListSerializer(many=True, read_only=True)
    artist = serializers.StringRelatedField()

    class Meta:
        model = Album
        fields = ('name', 'artist', 'year', 'tracks')


class ArtistListSerializer(serializers.ModelSerializer):

    album = AlbumListSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('name', 'album')
