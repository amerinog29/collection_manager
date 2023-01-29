from django.contrib import admin
from django.urls import path, include

from .views import *

collectionpatterns = []

musicianpatterns = [
    path('listar', artist_list, name='artist_list'),
    path('crear', create_artist, name='create_artist'),
    path('editar/<pk>', edit_artist, name='edit_artist'),
    path('eliminar/<pk>', delete_artist, name='delete_artist'),
]

albumpatterns = [
    path('listar', album_list, name='album_list'),
    path('crear', create_album, name='create_album'),
    path('editar/<pk>', edit_album, name='edit_album'),
    path('eliminar/<pk>', delete_album, name='delete_album'),
]

genrepatterns = [
    path('listar', genre_list, name='genre_list'),
    path('crear', create_genre, name='create_genre'),
    path('editar/<pk>', edit_genre, name='edit_genre'),
    path('eliminar/<pk>', delete_genre, name='delete_genre'),
]

urlpatterns = [
    # path('', test, name='test'),
    path('coleccion/', include(collectionpatterns)),
    path('artista/', include(musicianpatterns)),
    path('album/', include(albumpatterns)),
    path('genero/', include(genrepatterns)),
]