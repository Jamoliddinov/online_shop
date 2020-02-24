from django.contrib import admin

from shop.models import Category, Product, Cart, ProductColor, ProductRating, ProductSize, ProductPhoto

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductColor)
admin.site.register(ProductRating)
admin.site.register(ProductSize)
admin.site.register(ProductPhoto)
admin.site.register(Cart)
