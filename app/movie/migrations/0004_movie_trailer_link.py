# Generated by Django 4.0.1 on 2022-06-30 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_movie_dash_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trailer_link',
            field=models.URLField(null=True),
        ),
    ]
