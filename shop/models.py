from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255)

    def str(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    img = models.ImageField(null=True)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()
    link = models.URLField()
    categories = models.ManyToManyField(Category)

    @property
    def rating(self):
        p = 0
        productratings = self.ProductRating.all()
        for productrating in productratings:
            p += productrating.rating
        return p / len(productratings) if p > 0 else 0

class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_sizes')
    size = models.FloatField()


class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_colors')
    color = models.CharField(max_length=15)


class Cart(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='carts')

    @property
    def sum(self):
        s = 0
        cartproducts = self.cartproducts.all()
        for cartproduct in cartproducts:
            s += cartproduct.product.price * cartproduct.quantity
        return s


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='CartProduct')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cartproducts')
    quantity = models.PositiveIntegerField()

class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="productphotos")
    photo = models.ImageField(upload_to="imageProduct")

class ProductRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="productratings",null=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="productratings")
    title = models.CharField(max_length=255,null=True)
    description = models.CharField(max_length=255,null=True)
    rating = models.PositiveIntegerField()

    class Meta:
        unique_together = ['product', 'user']
