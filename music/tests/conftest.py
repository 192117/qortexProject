from factories import AlbumFactory, AlbumWithSongFactory, ArtistFactory, SongFactory, TrackFactory
from pytest_factoryboy import register

register(ArtistFactory)
register(AlbumFactory)
register(SongFactory)
register(TrackFactory)
register(AlbumWithSongFactory)
