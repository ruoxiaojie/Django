from django.shortcuts import render, redirect, HttpResponse
from rbac import models
from rbac.service import rbac


def login(request):
    if request.method == 'GET':
        return render(request, 'crm/login.html')
    else:
        from rbac import models
        from rbac.service import rbac

        user = request.POST.get('username')
        pwd = request.POST.get('password')
        user = models.User.objects.filter(username=user, password=pwd).first()
        if user:
            rbac.initial_permission(request, user)
            return redirect('/index/')
        else:
            return render(request, 'crm/login.html')


def index(request):
    return render(request, 'crm/index.html')
