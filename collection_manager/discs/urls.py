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

albumpatterns = []

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