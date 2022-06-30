from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    name = models.CharField(max_length=150)
    poster = models.ImageField()
    director_name = models.CharField(max_length=100)
    rate = models.FloatField(validators=[
        MaxValueValidator(10),
        MinValueValidator(0)
    ])
    description = models.TextField()
    dash_mode = models.BooleanField(default=False)
    trailer_link = models.URLField(null=True)

    def __str__(self):
        return self.name
