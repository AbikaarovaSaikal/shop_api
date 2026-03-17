from django.db import models

from users.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, 
                                 null=True, blank=True, related_name='products')
    owner = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

CHOICES = (
    (i, i) for i in range(1, 6)
)

class Review(models.Model):
    text = models.TextField(max_length=460)
    stars = models.IntegerField(choices=CHOICES, default=3)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='reviews')

    def __str__(self):
        return self.text