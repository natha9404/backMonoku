# Generated by Django 3.1.3 on 2021-02-20 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_auto_20210220_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='csv')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
