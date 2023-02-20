from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at the song ranking index.")


def playlist(request, playlist_id):
    return HttpResponse(f"You're looking at playlist {playlist_id}.")


def playlist_rank(request, playlist_id):
    return HttpResponse(f"You're ranking songs in playlist {playlist_id}.")


def user(request, user_id):
    return HttpResponse(f"You're viewing user {user_id}'s playlists.")
