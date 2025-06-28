
from django.contrib import admin
from django.urls import path, include

from . import views 


app_name = 'kontak'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
]