from django.conf.urls import url
from django.contrib import admin
from Mybook import views

urlpatterns = [
    url(r'^add/', views.add),
    url(r'^delete/', views.delete),
    url(r'^show/', views.show),
    url(r'^modify/', views.modify),

]
