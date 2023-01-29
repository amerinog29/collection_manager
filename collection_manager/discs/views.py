from django.shortcuts import render, redirect

# Create your views here.
from datetime import datetime as dt
from .models import Artist, Genre, Album


def artist_list(request):
	artists = Artist.objects.all()
	context = {'artists': artists}
	
	return render(request, 'artist/artist_list.html', context)


def create_artist(request):
	if request.method == 'POST':
		Artist.objects.create(photo=request.FILES.get('photo'), name=request.POST.get('name'))
		
		return redirect('artist_list')
	
	return render(request, 'artist/create_artist.html')


def edit_artist(request, pk):
	if request.method == 'POST':
		if 'photo' in request.FILES:
			defaults = {'photo': request.FILES.get('photo'), 'name': request.POST.get('name')}
		else:
			defaults = {'name': request.POST.get('name')}
			
		Artist.objects.update_or_create(pk=pk, defaults=defaults)
		
		return redirect('artist_list')
	
	else:
		artist = Artist.objects.get(pk=pk)
	
	return render(request, 'artist/create_artist.html', {'artist': artist})


def delete_artist(request, pk):
	try:
		artist = Artist.objects.get(pk=pk)
		artist.delete()
		
		return redirect('artist_list')
		
	except Artist.DoesNotExist:
		return redirect('artist_list')


def genre_list(request):
	genres = Genre.objects.all()
	context = {'genres': genres}
	
	return render(request, 'genre/genre_list.html', context)


def create_genre(request):
	if request.method == 'POST':
		Genre.objects.create(name=request.POST.get('name'))
		
		return redirect('genre_list')
	
	return render(request, 'genre/create_genre.html')


def edit_genre(request, pk):
	if request.method == 'POST':
		defaults = {'name': request.POST.get('name')}
		
		Genre.objects.update_or_create(pk=pk, defaults=defaults)
		
		return redirect('genre_list')
	
	else:
		genre = Genre.objects.get(pk=pk)
	
	return render(request, 'genre/create_genre.html', {'genre': genre})


def delete_genre(request, pk):
	try:
		genre = Genre.objects.get(pk=pk)
		genre.delete()
		
		return redirect('genre_list')
	
	except Artist.DoesNotExist:
		return redirect('genre_list')


def album_list(request):
	albums = Album.objects.all()
	context = {'albums': albums}
	
	return render(request, 'album/album_list.html', context)


def create_album(request):
	if request.method == 'POST':
		release_date = dt.strptime(request.POST.get('release_date'), '%d/%m/%Y')
		Album.objects.create(photo=request.FILES.get('photo'), name=request.POST.get('name'), release_date=release_date, artist_id=request.POST.get('artist_id'))
		
		return redirect('album_list')
	else:
		artists = Artist.objects.all()
		context = {'artists': artists}
	
	return render(request, 'album/create_album.html', context)


def edit_album(request, pk):
	if request.method == 'POST':
		defaults = {}
		if 'photo' in request.FILES:
			defaults['photo'] = request.FILES.get('photo')
		
		release_date = dt.strptime(request.POST.get('release_date'), '%d/%m/%Y')
		defaults['name'] = request.POST.get('name')
		defaults['release_date'] = release_date
		defaults['artist_id'] = request.POST.get('artist_id')
		
		Album.objects.update_or_create(pk=pk, defaults=defaults)
		
		return redirect('album_list')
	
	else:
		album = Album.objects.get(pk=pk)
		artists = Artist.objects.all()
		context = {'album': album, 'artists': artists}
	
	return render(request, 'album/create_album.html', context)


def delete_album(request, pk):
	try:
		album = Album.objects.get(pk=pk)
		album.delete()
		
		return redirect('album_list')
	
	except Artist.DoesNotExist:
		return redirect('album_list')
	
		
		