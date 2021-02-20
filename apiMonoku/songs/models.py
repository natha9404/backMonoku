from django.db import models

# Create your models here.

class Band(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Song(models.Model):
    external_id = models.IntegerField(null=False)
    #date = models.DateTimeField()
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    subgenre = models.CharField(max_length=100)
    similar_band = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    instrument = models.TextField()

    band = models.ForeignKey(
        Band, related_name="bands_songs", on_delete=models.CASCADE
    )

    artist = models.ForeignKey(
        Artist, related_name="artists_songs", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
