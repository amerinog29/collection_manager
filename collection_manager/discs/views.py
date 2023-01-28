from django.shortcuts import render, redirect

# Create your views here.
from .models import Artist


def artist_list(request):
	artists = Artist.objects.all()
	context = {'artists': artists}
	
	return render(request, 'artist/artist_list.html', context)


def create_artist(request):
	if request.method == 'POST':
		Artist.objects.create(logo=request.FILES.get('logo'), name=request.POST.get('name'))
		
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
	
		
		