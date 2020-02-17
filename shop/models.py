from django.db import models

# Create your models here.


from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=15)
    # id = models.CharField(max_length=15)


class Product(models.Model):
    name = models.CharField(max_length=15)
    title = models.CharField(max_length=15)
    img = models.ImageField(null=True)
    description = models.CharField(max_length=15)
    quantity = models.IntegerField()
    prise = models.FloatField()
    link = models.URLField()
    categories = models.ManyToManyField(Category)


class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ProductSizes')
    size = models.FloatField()


class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ProductColors')
    color = models.CharField(max_length=15)


class Cart(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='Carts')


class ProductRating(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='ProductRating')
    rating = models.IntegerField()
