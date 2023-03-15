import pytest
from rest_framework import status
from rest_framework.test import APIClient

from music.models import Album, Artist, Song, Track
from music.serializers import TrackListSerializer

client = APIClient()


@pytest.mark.django_db
class TestTrackAPIViews:

    def test_success_create_track(self, song, album):

        data = {
            'song': song.name,
            'album': album.name,
            'track_number': 5
        }

        response = client.post(
            '/api/v1/track/create/',
            data=data
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['song'] == song.name
        assert response.data['album'] == album.name
        assert response.data['track_number'] == 5

    def test_list_no_track(self):

        response = client.get('/api/v1/track/')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 0

    def test_list_with_track(self, song, album):

        response = client.get('/api/v1/track/')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 1
        assert response.json()[0]['song'] == song.name
        assert response.json()[0]['album'] == album.name

    def test_detail_track(self, track):

        response = client.get(f'/api/v1/track/{track.pk}')

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == TrackListSerializer(track).data

    def test_put_track(self, track):

        data = {
            'song': track.song.name,
            'track_number': 2,
            'album': track.album.name
        }

        response = client.put(
            f'/api/v1/track/{track.pk}',
            data=data
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.json()['track_number'] == data['track_number']

    def test_patch_track(self, track, song, album):

        data = {
            'song': song.name,
            'track_number': 3,
            'album': album.name
        }

        response = client.patch(
            f'/api/v1/track/{track.pk}',
            data=data
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.json()['track_number'] == data['track_number']

    def test_delete_track(self, track):

        response = client.delete(f'/api/v1/track/{track.pk}')

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_track_str_representation(self):

        artist = Artist.objects.create(name='Test Artist')
        album = Album.objects.create(name='Test Album', artist=artist, year='2022-01-01')
        song = Song.objects.create(name='Test Song')
        track = Track.objects.create(album=album, song=song, track_number=1)

        assert str(track) == 'Test Song-Test Album-1'
