from django.urls import path

from .views import (AlbumCreateView, AlbumListView, AlbumView, ArtistCreateView, ArtistListView, ArtistView,
                    SongCreateView, SongListView, SongView)

urlpatterns = [
    path('artist/', ArtistListView.as_view()),
    path('artist/<int:pk>', ArtistView.as_view()),
    path('artist/create/', ArtistCreateView.as_view()),
    path('album/', AlbumListView.as_view()),
    path('album/<int:pk>', AlbumView.as_view()),
    path('album/create/', AlbumCreateView.as_view()),
    path('song/', SongListView.as_view()),
    path('song/<int:pk>', SongView.as_view()),
    path('song/create/', SongCreateView.as_view())
]
