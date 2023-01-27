from django.db import models

# Create your models here.


class Musician(models.Model):
	photo = models.ImageField(upload_to='photos')
	name = models.CharField(max_length=150)
	
	
class Album(models.Model):
	name = models.CharField(max_length=100)
	release_date = models.DateField()
	musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='musician')


class Observations(models.Model):
	text = models.TextField()
	date = models.DateTimeField(auto_now=True)
	
	
class Genre(models.Model):
	name = models.CharField(max_length=150)


class Disc(models.Model):
	artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
	country = models.CharField(max_length=20)
	observation = models.ForeignKey(Observations, on_delete=models.CASCADE)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
