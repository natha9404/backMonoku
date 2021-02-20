from django.contrib import admin

from .models import Artist, Band, Genre, Subgenre, Song

# Register your models here.
admin.site.register(Artist)
admin.site.register(Band)
admin.site.register(Genre)
admin.site.register(Subgenre)
admin.site.register(Song)
