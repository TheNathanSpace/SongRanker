from django.contrib import admin

from .models import Playlist, Song, PlaylistSongsWins

admin.site.register(Playlist)
admin.site.register(Song)
admin.site.register(PlaylistSongsWins)
