# Generated by Django 4.1.5 on 2023-01-29 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discs', '0005_rename_musician_artist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='photo',
            field=models.ImageField(default='album/', upload_to='album'),
            preserve_default=False,
        ),
    ]
