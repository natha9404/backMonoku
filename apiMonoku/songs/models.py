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

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subgenre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Song(models.Model):
    extern_id = models.IntegerField(null=False)
    #date = models.DateTimeField()
    name = models.CharField(max_length=100)
    similar_band = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    instrument = models.TextField()

    band = models.ForeignKey(
        Band, related_name="bands", on_delete=models.CASCADE
    )

    artist = models.ForeignKey(
        Artist, related_name="artists", on_delete=models.CASCADE
    )

    genre = models.ForeignKey(
        Genre, related_name="genres", on_delete=models.CASCADE
    )

    subgenre = models.ForeignKey(
        Subgenre, related_name="subgenres", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name