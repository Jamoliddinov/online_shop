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


@register.simple_tag(takes_context=True)
def category_checker(context, category_id):
    list = context['request'].GET.getlist('categories')
    return str(category_id) in list


@register.filter(name='product_count')
def product_counter_by_category(id):
    if id:
        return Product.objects.filter(categories=id).count()
