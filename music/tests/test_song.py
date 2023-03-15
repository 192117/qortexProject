import pytest
from factories import faker
from rest_framework import status
from rest_framework.test import APIClient

from music.models import Song
from music.serializers import SongCreateSerializer

client = APIClient()


@pytest.mark.django_db
class TestSongAPIViews:

    def test_success_create_song(self, song):

        data = {
            'name': faker.unique.name(),
        }

        response = client.post(
            '/api/v1/song/create/',
            data=data
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == data['name']

    def test_detail_song(self, song):

        response = client.get(f'/api/v1/song/{song.pk}')

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == SongCreateSerializer(song).data

    def test_put_song(self, song):

        data = {
            'name': 'New name song',
        }

        response = client.put(
            f'/api/v1/song/{song.pk}',
            data=data
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.json()['name'] == data['name']

    def test_patch_song(self, song):

        data = {
            'name': 'New name song patch',
        }

        response = client.patch(
            f'/api/v1/song/{song.pk}',
            data=data
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.json()['name'] == data['name']

    def test_delete_song(self, song):

        response = client.delete(f'/api/v1/song/{song.pk}')

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_song_str_representation(self):

        song = Song.objects.create(name='Test Song')

        assert str(song) == 'Test Song'
