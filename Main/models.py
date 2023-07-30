from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class destinations(models.Model):
    name = models.CharField(max_length=100,unique=True, db_index=True)
    longitude = models.FloatField(max_length=100)
    latitude = models.FloatField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, message='Value must be greater than or equal to 0.'),
            MaxValueValidator(100, message='Value must be less than or equal to 100.')
        ]
    )
    