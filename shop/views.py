from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
from django.contrib.auth import authenticate, login
from django.urls import reverse

from shop.models import Category
from shop.models import Login
from shop.models import Error
from shop.models import Product
from shop.models import Index


def category_list(request):
    template = get_template('shop/category.html')
    category = Category.objects.all()
    body = template.render({'category': category})
    return HttpResponse(body)


# do not touch it
# def notFoundPage_list(request):
#     template = get_template('shop/404.html')
#     notFoundPage = Error.objects.all()
#     body = template.render({'notFoundPage': notFoundPage})
#     return HttpResponse(body)

def login_list(request):
    if request.method == 'GET':
        template = get_template('shop/login.html')
        body = template.render({})
        return HttpResponse(body)
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            # sucessful login
            login(request, user)
            return HttpResponseRedirect(reverse('product_list'))
        else:
            return HttpResponseRedirect(reverse('login'))


def product_list(request):
    template = get_template('shop/product.html')
    product = Product.objects.all()
    body = template.render({'product': product})
    return HttpResponse(body)


def index_list(request):
    template = get_template('shop/index-7.html')
    index = Index.objects.all()
    body = template.render({'index': index})
    return HttpResponse(body)
