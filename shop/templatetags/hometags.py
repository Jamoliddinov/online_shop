from django.contrib.auth import get_user_model
from django import template

from shop.models import Product

register = template.Library()


@register.simple_tag
def counter():
    user = get_user_model()
    return user


@register.filter
def total_sum(card_products):
    sum = 0
    for cart_product in card_products:
        sum += cart_product.quantity * cart_product.product.price
    return sum


@register.filter
def category_count_product(request, id):
    list = request.GET.getlist('categories')
    return True if str(id) in list else False


@register.filter(name='product_count')
def product_counter_by_category(id):
    if id:
        return Product.objects.filter(categories=id).count()
