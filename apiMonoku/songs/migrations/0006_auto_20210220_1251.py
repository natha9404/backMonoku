# Generated by Django 3.1.3 on 2021-02-20 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0005_csv'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='albums',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='duration',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='csv',
            name='file_name',
            field=models.FileField(upload_to='csvs'),
        ),
    ]