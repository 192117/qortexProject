from factories import AlbumFactory, AlbumWithSongFactory, ArtistFactory, SongFactory, TrackFactory
from pytest_factoryboy import register

register(ArtistFactory, 'artist')
register(AlbumFactory, 'album')
register(SongFactory, 'song')
register(TrackFactory, 'track')
register(AlbumWithSongFactory, 'album_with_song')
