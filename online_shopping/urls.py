"""online_shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from online_shopping import settings
from shop.views import category_list, index_list, login_list, product_detail, cart, add_to_cart, logout_user, index, \
    del_product_from_cart, cart_checkout
from userProfile.views import register
from django.conf.urls.i18n import i18n_patterns

app_name = "shops"

urlpatterns = [

]
urlpatterns += i18n_patterns(
    path('category/', category_list, name='category_list'),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('index/', index_list),
    path('login/', login_list, name='login'),
    path('register/', register, name='register'),
    path('cart/', cart, name='cart'),
    path('cart/add-to-cart/<int:pk>/<int:quantity>/', add_to_cart, name='add_to_cart'),
    path('cart/del-product-from-cart/<int:id>/', del_product_from_cart, name='del_product_from_cart'),
    path('product/<int:pk>', product_detail, name='product_detail'),
    path('logout/', logout_user, name='logout_user'),
    path('check-out/', cart_checkout, name='cart_checkout'),
    # path('404/', notFoundPage_list)
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
