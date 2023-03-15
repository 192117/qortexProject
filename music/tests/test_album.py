import pytest
from factories import faker
from rest_framework import status
from rest_framework.test import APIClient

from music.models import Album, Artist
from music.serializers import AlbumListSerializer

client = APIClient()


@pytest.mark.django_db
class TestAlbumAPIViews:

    def test_success_create_album(self, album):

        data = {
            'name': faker.unique.name(),
            'artist': album.artist.name,
            'year': album.year
        }

        response = client.post(
            '/api/v1/album/create/',
            data=data
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == data['name']
        assert response.data['artist'] == data['artist']
        assert response.data['year'] == data['year']

    def test_list_no_album(self):

        response = client.get('/api/v1/album/')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 0

    def test_list_with_album(self, album, artist):

        response = client.get('/api/v1/album/')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 1
        assert response.json()[0]['name'] == album.name
        assert response.json()[0]['year'] == album.year
        assert response.json()[0]['artist'] == artist.name

    def test_detail_album(self, album):

        response = client.get(f'/api/v1/album/{album.pk}')

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == AlbumListSerializer(album).data

    def test_put_album(self, album):

        data = {
            'name': 'New name album',
            'year': album.year
        }

        response = client.put(
            f'/api/v1/album/{album.pk}',
            data=data
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.json()['name'] == data['name']

    def test_patch_album(self, album):

        data = {
            'name': 'New name album patch',
            'year': album.year
        }

        response = client.patch(
            f'/api/v1/album/{album.pk}',
            data=data
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.json()['name'] == data['name']

    def test_delete_album(self, album):

        response = client.delete(f'/api/v1/album/{album.pk}')

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_album_str_representation(self):

        artist = Artist.objects.create(name='Test Artist')
        album = Album.objects.create(name='Test Album', artist=artist, year='2022-01-01')

        assert str(album) == 'Test Album'
