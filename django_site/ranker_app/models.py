from django.db import models


class Playlist(models.Model):
    id = models.TextField(primary_key = True)
    owner_id = models.TextField()
    name = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.name


class Song(models.Model):
    id = models.TextField(primary_key = True)
    name = models.TextField()
    album = models.TextField()
    artist = models.TextField()
    image = models.TextField()

    def __str__(self):
        return f"{self.artist} - {self.name}"


class PlaylistSongsWins(models.Model):
    playlist_id = models.ForeignKey(Playlist, on_delete = models.CASCADE)
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)
    song_wins = models.IntegerField(default = 0)

    def __str__(self):
        return f"{self.song_id} - {self.song_wins}"
