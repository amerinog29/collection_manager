# Generated by Django 4.1.5 on 2023-01-31 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discs', '0007_disc_name_disc_photo_disc_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disc',
            name='country',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='disc',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='discs.genre'),
        ),
        migrations.AlterField(
            model_name='disc',
            name='observation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='discs.observation'),
        ),
        migrations.AlterField(
            model_name='disc',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]
