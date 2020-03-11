from modeltranslation.translator import TranslationOptions, translator

from shop.models import Product


class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Product, ProductTranslationOptions)
