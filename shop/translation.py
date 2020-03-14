from modeltranslation.translator import TranslationOptions, translator

from shop.models import Product, ProductRating, ProductColor


class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class RatingTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class ColorTranslationOptions(TranslationOptions):
    fields = ('color',)


translator.register(ProductColor, ColorTranslationOptions)
translator.register(ProductRating, RatingTranslationOptions)
translator.register(Product, ProductTranslationOptions)
