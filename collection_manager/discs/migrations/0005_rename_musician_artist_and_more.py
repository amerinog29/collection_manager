# Generated by Django 4.1.5 on 2023-01-27 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discs', '0004_remove_musician_logo_musician_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Musician',
            new_name='Artist',
        ),
        migrations.RenameModel(
            old_name='Observations',
            new_name='Observation',
        ),
        migrations.RemoveField(
            model_name='album',
            name='musician',
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='artist', to='discs.artist'),
            preserve_default=False,
        ),
    ]
