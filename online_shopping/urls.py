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
from django.urls import path
from django.http import HttpResponse

from online_shopping import settings
from shop.views import category_list, index_list, login_list, product_list, product_detail
from userProfile.views import register


def index(request):
   return HttpResponse('Hello World')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('category/', category_list, name='category_list'),
    path('index/', index_list),
    path('login/', login_list, name='login'),
    path('register/', register, name='register'),
    path('product/<int:pk>', product_detail, name='product_detail'),
    # path('404/', notFoundPage_list)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
