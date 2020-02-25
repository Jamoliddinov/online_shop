from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse


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
    return HttpResponse()


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('login'))

