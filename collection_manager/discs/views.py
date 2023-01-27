from django.shortcuts import render, redirect

# Create your views here.
from .models import Artist


def artist_list(request):
	artists = Artist.objects.all()
	context = {'artists': artists}
	return render(request, 'artist/artist_list.html', context)


def create_artist(request):
	if request.method == 'POST':
		print(request.POST)
		print(request.FILES)
		Artist.objects.create(logo=request.FILES.get('logo'), name=request.POST.get('name'))
		
		return redirect('artist_list')
	
	return render(request, 'artist/create_artist.html')
