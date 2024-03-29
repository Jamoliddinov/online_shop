from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from shop.models import Category, Product, Cart, ProductColor, ProductRating, ProductSize, ProductPhoto, CartProduct

class ProductAdmin(TranslationAdmin):
    pass

class RatingAdmin(TranslationAdmin):
    pass

class ColorAdmin(TranslationAdmin):
    pass


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductColor, ColorAdmin)
admin.site.register(ProductRating, RatingAdmin)
admin.site.register(ProductSize)
admin.site.register(ProductPhoto)
admin.site.register(CartProduct)
admin.site.register(Cart)
