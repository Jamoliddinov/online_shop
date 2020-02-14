from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse


def category_list(request):
    template = get_template('shop/category.html')
    body = template.render({})
    return HttpResponse(body)
