
from django.core.validators import MinValueValidator
from django.db import models
# Create your models here.


class Product(models.Model):
    title = models.CharField(blank=False, null=False, max_length=200)
    description = models.TextField(blank=False, null=False)
    price = models.FloatField(validators=[MinValueValidator(0.1)])
    imageUrl = models.URLField(max_length = 200)
    isFavourite = models.BooleanField(default=False)
