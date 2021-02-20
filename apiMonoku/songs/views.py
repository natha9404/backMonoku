from django.shortcuts import render

from .forms import CsvModelForm
from .models import Csv, Song, Artist, Band

import csv

# Create your views here.
def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if  form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get()
        with open(obj.file_name.path, 'r') as f:
            reader =  csv.reader(f)

            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    row = "".join(row)
                    row = row.replace(";", " ")
                    row = row.split()
                    artist = Artist.objects.get_or_create(name= row[5])
                    band = Band.objects.get_or_create(name= row[4])
                    song = Song.objects.create(
                        external_id = row[1],
                        name = row[2],
                        album = row[3],
                        duration  = row[6],
                        similar_band = row[7],
                        tag = row[8],
                        instrument = row[9],
                        artist = this.artist,
                        band = this.band)
                    song.save()
    return render(request, './base.html', {'form': form})