from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.loader import get_template
from django.contrib.auth import authenticate, login
from django.urls import reverse

from shop.models import Category, ProductSize, ProductColor, ProductPhoto, ProductRating
from shop.models import Product


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


def product_list(request, pk):
    template = get_template('shop/product.html')
    product = Product.objects.filter(pk=pk).all()
    body = template.render({'product': product})
    return HttpResponse(body)


def index_list(request):
    template = get_template('shop/index-7.html')
    index = Index.objects.all()
    body = template.render({'index': index})
    return HttpResponse(body)


def product_detail(request, pk):
    try:
        product = Product.objects.filter(pk=pk).get()
    except ObjectDoesNotExist:
        raise Http404()
    product_sizes = ProductSize.objects.filter(product=product).all()
    product_colors = ProductColor.objects.filter(product=product).all()
    product_photos = ProductPhoto.objects.filter(product=product).all()
    product_ratings = ProductRating.objects.filter(product=product).all()
    template = get_template('shop/product.html')
    r = template.render({'product': product, 'product_sizes': product_sizes, 'product_colors': product_colors, 'product_photos':product_photos , 'product_ratings':product_ratings})
    return HttpResponse(r)