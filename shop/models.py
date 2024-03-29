from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

UserModel = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(null=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    link = models.URLField(null=True, blank=True)
    categories = models.ManyToManyField(Category, blank=True)

    @property
    def rating(self):
        p = 0
        productratings = self.productratings.all()
        for productrating in productratings:
            p += productrating.rating
        return p / len(productratings) if p > 0 else 0

    @property
    def rating_percentage(self):
        return self.rating / 5 * 100

    @property
    def rating_count(self):
        return len(self.productratings.all())

    @property
    def is_new(self):
        return True


class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_sizes')
    size = models.FloatField()


class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_colors')
    color = models.CharField(max_length=15)


class Cart(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='carts')
    checked_at = models.DateTimeField(null=True)

    @property
    def sum(self):
        s = 0
        cartproducts = self.cartproducts.all()
        for cartproduct in cartproducts:
            s += cartproduct.product.price * cartproduct.quantity
        return s


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cartproducts')
    quantity = models.PositiveIntegerField()


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="productphotos")
    photo = models.ImageField(upload_to="imageProduct")


class ProductRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="productratings", null=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="productratings")
    title = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ['product', 'user']
