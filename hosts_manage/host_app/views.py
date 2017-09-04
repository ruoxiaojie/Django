from django.shortcuts import render,HttpResponse,redirect

# Create your views here.





def login(request):


    return render(request,"login.html")

def index(request):
    pass

def logout(request):

    return redirect('/login.html')

