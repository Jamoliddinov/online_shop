from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Index
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from shop.models import ProductSize, ProductColor, ProductPhoto, ProductRating, Product, Cart, CartProduct


def category_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page = request.GET.get('page', 1)
    products_pagination = paginator.page(page)
    return render(request, 'shop/category.html', {'products_pagination': products_pagination, 'user': request.user})


@login_required(login_url='/login')
def add_to_cart(request, pk, quantity=1):
    cart, created = Cart.objects.get_or_create(user=request.user, checked_at__isnull=True)
    new_product_cart = CartProduct(cart=cart, product_id=pk, quantity=quantity)
    new_product_cart.save()
    return redirect(reverse('cart'))


# do not touch it
# def notFoundPage_list(request):
#     template = get_template('shop/404.html')
#     notFoundPage = Error.objects.all()
#     body = template.render({'notFoundPage': notFoundPage})
#     return HttpResponse(body)

def login_list(request):
    if request.method == 'GET':
        # template = get_template('shop/login.html')
        # body = template.render({'request': request})
        return render(request, 'shop/login.html', {'user': request.user})
    else:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user:
            # sucessful login
            login(request, user)
            return HttpResponseRedirect(reverse('category_list'))
        else:
            return HttpResponseRedirect(reverse('login'))


def product_list(request, pk):
    product = Product.objects.filter(pk=pk).all()
    return render(request, 'shop/product.html', {'product': product})


def cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, checked_at__isnull=True)

        cart_products = CartProduct.objects.filter(cart=cart)
        return render(request, 'shop/cart.html', {'cart_products': cart_products})
    else:
        return HttpResponseRedirect(reverse('category_list'))


def index_list(request):
    index = Index.objects.all()
    return render(request, 'shop/index-7.html', {'index': index})


def index(request):
    return render(request, 'shop/index-2.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('category_list'))


def product_detail(request, pk):
    try:
        product = Product.objects.filter(pk=pk).get()
    except ObjectDoesNotExist:
        raise Http404()
    product_sizes = ProductSize.objects.filter(product=product)
    product_colors = ProductColor.objects.filter(product=product).all()
    product_photos = ProductPhoto.objects.filter(product=product).all()
    product_ratings = ProductRating.objects.filter(product=product).all()
    return render(request, 'shop/product.html',
                  {'product': product, 'product_sizes': product_sizes, 'product_colors': product_colors,
                   'product_photos': product_photos, 'product_ratings': product_ratings})
