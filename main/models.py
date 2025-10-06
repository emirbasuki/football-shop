import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('watch', 'Watch'),
        ('belt', 'Belt'),
        ('shirt', 'Shirt'),
        ('pants', 'Pants'),
        ('bag', 'Bag'),
        ('earphone', 'Earphone'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=2)

    product_views = models.IntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
    def increment_views(self):
        self.product_views += 1
        self.save()

