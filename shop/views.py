from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from shop.models import Category


def category_list(request):
    template = get_template('shop/categories.html')
    categories = Category.objects.all()
    body = template.render({'categories': categories})
    return HttpResponse(body)