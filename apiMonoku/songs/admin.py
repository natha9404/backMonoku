from django.contrib import admin

from .models import Artist, Band, Song, Csv

# Register your models here.
admin.site.register(Artist)
admin.site.register(Band)
admin.site.register(Song)
admin.site.register(Csv)
