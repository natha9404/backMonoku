from django.contrib import admin

from .models import Artist, Band, Song

# Register your models here.
admin.site.register(Artist)
admin.site.register(Band)
admin.site.register(Song)
