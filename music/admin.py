from django.contrib import admin

from .models import Album, Artist, Song, Track


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class TrackAInlineAdmin(admin.TabularInline):
    model = Track
    extra = 1


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (TrackAInlineAdmin,)
    list_display = ('name', 'year',)
    search_fields = ('name', 'year',)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    inlines = (TrackAInlineAdmin,)
    list_display = ('name',)
    search_fields = ('name',)
