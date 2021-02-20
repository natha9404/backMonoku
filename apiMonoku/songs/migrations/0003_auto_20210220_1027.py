# Generated by Django 3.1.3 on 2021-02-20 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_auto_20210220_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artists_songs', to='songs.artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='band',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bands_songs', to='songs.band'),
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genres_songs', to='songs.genre'),
        ),
        migrations.AlterField(
            model_name='song',
            name='subgenre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subgenres_songs', to='songs.subgenre'),
        ),
    ]