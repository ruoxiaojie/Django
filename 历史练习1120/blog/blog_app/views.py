from django.shortcuts import render,redirect,HttpResponse




def home(request):
    return HttpResponse("hello world")

