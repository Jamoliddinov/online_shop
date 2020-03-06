from django.contrib.auth import get_user_model
from django.template import Library

register = Library()


@register.simple_tag
def counter():
    user = get_user_model()
    return user


# @register.filter
# def multiply(value, arg):
#     return value * arg
