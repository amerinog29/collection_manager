from django.shortcuts import render, redirect

# Create your views here.
from datetime import datetime as dt
from .models import Artist, Genre, Album, Disc, Observation


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


def disc_list(request):
	discs = Disc.objects.all()
	context = {'discs': discs}
	
	return render(request, 'collection/collection_list.html', context)


def validate_data(request, action):
	tmp_json = {}
	
	if 'photo' not in request.POST:
		tmp_json['photo'] = request.FILES.get('photo')
	
	if request.POST.get('release_date') != '':
		tmp_json['release_date'] = dt.strptime(request.POST.get('release_date'), '%d/%m/%Y')
	
	if request.POST.get('observation') != '' and action != 'edit':
		obs_temp = Observation.objects.create(text=request.POST.get('observation'))
		tmp_json['observation_id'] = obs_temp.pk
		
	return tmp_json


def generate_json_data(request, action):
	data = {
		'name': request.POST.get('name'),
		'artist_id': request.POST.get('artist_id'),
		'country': request.POST.get('country'),
		'genre_id': request.POST.get('genre_id')
	}
	
	tmp_json = validate_data(request, action)
	if len(tmp_json) != 0:
		data.update(tmp_json)
		
	return data
	

def create_disc(request):
	if request.method == 'POST':
		print(request.POST)
		data = generate_json_data(request)
		Disc.objects.create(**data)
	
		return redirect('disc_list')
	else:
		artists = Artist.objects.all()
		genres = Genre.objects.all()
		context = {'artists': artists, 'genres': genres}
	
	return render(request, 'collection/create_collection.html', context)


def edit_disc(request, pk):
	if request.method == 'POST':
		disc = Disc.objects.get(pk=pk)
		if disc.observation:
			obs = Observation.objects.get(pk=disc.observation_id)
			obs.text = request.POST.get('observation')
			obs.save()
		
		defaults = generate_json_data(request, 'edit')
		Disc.objects.update_or_create(pk=pk, defaults=defaults)
		
		return redirect('disc_list')
	
	else:
		disc = Disc.objects.get(pk=pk)
		artists = Artist.objects.all()
		genres = Genre.objects.all()
		context = {'disc': disc, 'artists': artists, 'genres': genres}
	
	return render(request, 'collection/create_collection.html', context)


def delete_disc(request, pk):
	try:
		disc = Disc.objects.get(pk=pk)
		disc.delete()
		
		return redirect('disc_list')
	
	except Artist.DoesNotExist:
		return redirect('album_list')
	
		
		