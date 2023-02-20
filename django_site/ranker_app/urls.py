from django.urls import path

from . import views

urlpatterns = [
    # ex: /ranker/
    path("", views.index, name = "index"),

    # ex: /ranker/[playlist_id]/
    path("<str:playlist_id>/", views.playlist, name = "detail"),

    # ex: /ranker/[playlist_id]]/rank/
    path("<str:playlist_id>/rank/", views.playlist_rank, name = "results"),

    # ex: /[user_id]/
    path("<str:user_id>/", views.user, name = "user"),
]
