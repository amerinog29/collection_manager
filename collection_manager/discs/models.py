from django.db import models

# Create your models here.


class Artist(models.Model):
	photo = models.ImageField(upload_to='photos', default='disc/default_avatar.png')
	name = models.CharField(max_length=150)
	
	
class Album(models.Model):
	photo = models.ImageField(upload_to='album', default='default_album.jpg')
	name = models.CharField(max_length=100)
	release_date = models.DateField()
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artist')


class Observation(models.Model):
	text = models.TextField()
	date = models.DateTimeField(auto_now=True)
	
	
class Genre(models.Model):
	name = models.CharField(max_length=150)


class Disc(models.Model):
	photo = models.ImageField(upload_to='disc', default='disc/default_vinyl.png')
	name = models.CharField(max_length=100)
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
	country = models.CharField(max_length=20, null=True, blank=True)
	release_date = models.DateField(null=True)
	observation = models.ForeignKey(Observation, on_delete=models.CASCADE, null=True)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
