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

genrepatterns = []

urlpatterns = [
    # path('', test, name='test'),
    path('coleccion/', include(collectionpatterns)),
    path('artista/', include(musicianpatterns)),
    path('album/', include(albumpatterns)),
    path('genero/', include(genrepatterns)),
]