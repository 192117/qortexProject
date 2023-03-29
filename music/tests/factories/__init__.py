import random

import factory
from factory.django import DjangoModelFactory
from faker import Faker

from music.models import Album, Artist, Song, Track

faker = Faker()


class ArtistFactory(DjangoModelFactory):

    class Meta:
        model = Artist

    name = factory.LazyAttribute(lambda _: faker.unique.name())


class AlbumFactory(DjangoModelFactory):

    class Meta:
        model = Album

    name = factory.LazyAttribute(lambda _: faker.unique.name())
    artist = factory.SubFactory(ArtistFactory)
    year = '2022-04-06'


class SongFactory(DjangoModelFactory):

    class Meta:
        model = Song

    name = factory.LazyAttribute(lambda _: faker.unique.name())


class TrackFactory(DjangoModelFactory):

    class Meta:
        model = Track

    album = factory.SubFactory(AlbumFactory)
    song = factory.SubFactory(SongFactory)
    track_number = random.randint(1, 150)


class AlbumWithSongFactory(AlbumFactory):
    albumship = factory.RelatedFactory(
        TrackFactory,
        factory_related_name='tracks',
    )
