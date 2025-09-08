import uuid
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)

    stock = models.IntegerField(default=0)
    rating = models.DecimalField(default=0.0)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=2)

    def __str__(self):
        return self.name

