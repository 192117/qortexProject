from django.urls import path

from .views import (AlbumCreateView, AlbumListView, AlbumRUDView, ArtistCreateView, ArtistListView, ArtistRUDView,
                    SongCreateView, SongRUDView, TrackCreateView, TrackListView, TrackRUDView)

urlpatterns = [
    path('artist/create/', ArtistCreateView.as_view()),
    path('album/create/', AlbumCreateView.as_view()),
    path('song/create/', SongCreateView.as_view()),
    path('track/create/', TrackCreateView.as_view()),
    path('track/', TrackListView.as_view()),
    path('album/', AlbumListView.as_view()),
    path('artist/', ArtistListView.as_view()),
    path('artist/<int:pk>', ArtistRUDView.as_view()),
    path('album/<int:pk>', AlbumRUDView.as_view()),
    path('song/<int:pk>', SongRUDView.as_view()),
    path('track/<int:pk>', TrackRUDView.as_view()),

]
