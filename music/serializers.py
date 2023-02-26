from rest_framework import serializers

from .models import Album, Artist, Song, Track


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('name',)


class TrackSerializer(serializers.ModelSerializer):

    song = SongSerializer(many=False)
    album = serializers.StringRelatedField(many=False)

    class Meta:
        model = Track
        fields = ('song', 'track_number', 'album',)


class AlbumSerializer(serializers.ModelSerializer):

    artists = serializers.StringRelatedField(many=True)
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ('name', 'artists', 'year', 'tracks')


class ArtistSerializer(serializers.ModelSerializer):

    albums = AlbumSerializer(many=True)

    class Meta:
        model = Artist
        fields = ('name', 'albums',)
