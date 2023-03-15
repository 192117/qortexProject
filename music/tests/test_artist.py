import pytest
from factories import faker
from rest_framework import status
from rest_framework.test import APIClient

from music.models import Artist
from music.serializers import ArtistListSerializer

client = APIClient()


@pytest.mark.django_db
class TestArtistAPIViews:

    def test_success_create_artist(self):

        data = {
            'name': faker.unique.name(),

        }

        response = client.post(
            '/api/v1/artist/create/',
            data=data
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == data['name']

    def test_list_no_artist(self):

        response = client.get('/api/v1/artist/')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 0

    def test_list_with_artist(self, artist):

        response = client.get('/api/v1/artist/')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 1
        assert response.json()[0]['name'] == artist.name

    def test_detail_artist(self, artist):

        response = client.get(f'/api/v1/artist/{artist.pk}')

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == ArtistListSerializer(artist).data

    def test_put_artist(self, artist):

        data = {
            'name': 'New name',
        }

        response = client.put(
            f'/api/v1/artist/{artist.pk}',
            data=data
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.json()['name'] == data['name']

    def test_patch_artist(self, artist):

        data = {
            'name': 'New name patch',
        }

        response = client.patch(
            f'/api/v1/artist/{artist.pk}',
            data=data
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.json()['name'] == data['name']

    def test_delete_artist(self, artist):

        response = client.delete(f'/api/v1/artist/{artist.pk}')

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_artist_str_representation(self):

        artist = Artist.objects.create(name='Test Artist')

        assert str(artist) == 'Test Artist'
