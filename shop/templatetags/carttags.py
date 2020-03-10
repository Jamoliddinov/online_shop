from django import template

register = template.Library()


@register.filter(name='mul')
def mul(a1, a2):
    return round(a1 * a2, 3)
