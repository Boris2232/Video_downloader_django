from Download_videos.wsgi import *
from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from link_collector.views import collector
from regform.models import People
from Download_videos.wsgi import *


def index_1(request):
    if request.method == 'POST':
        login = request.POST['username']
        password = request.POST['password']
        new_user = People(name=login, password=password)
        new_user.save()
        return redirect("login/")
    return render(request, 'index.html')


def congrat(request):
    return render(request, 'congratulations.html')


def login_page(request):
    all_people = People.objects.all()
    s1 = []
    for i in all_people:
        s1.append([i.name, i.password])
    if request.method == 'POST':
        given_login = request.POST.get('username')
        given_pass = request.POST.get('password')
        redirected = False
        for i in range(len(s1)):
            if s1[i][0] == given_login and s1[i][1] == given_pass:
                return HttpResponseRedirect('/congrat')
    return render(request, 'login.html')
