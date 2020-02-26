from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse
from django.views import View

UserModel = get_user_model()

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


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            UserModel.objects.filter(username=email).get()
            return HttpResponseRedirect(reverse('login'))
        except ObjectDoesNotExist:
            user = UserModel.objects.create(username=email)
            user.set_password(password)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('category_list'))
    else:
        return HttpResponseNotAllowed(['POST'])


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('login'))

