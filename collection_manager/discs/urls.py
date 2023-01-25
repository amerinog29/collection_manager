from django.contrib import admin
from django.urls import path, include

from .views import test

collectionpatterns = []

musicianpatterns = []

albumpatterns = []

genrepatterns = []

urlpatterns = [
    path('', test, name='test'),
    path('coleccion/', include(collectionpatterns)),
    path('artista/', include(musicianpatterns)),
    path('album/', include(albumpatterns)),
    path('genero/', include(genrepatterns)),
]