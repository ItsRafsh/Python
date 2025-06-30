from django.contrib import admin
from django.urls import path
from . import views

app_name = 'movie'
urlpatterns = [
    path('update/<slug:up_slug>/', views.update, name='update'),
    path('delete/<slug:del_slug>/', views.delete, name='delete'),
    path('create/', views.create_mv, name='create_mv'),
    path('detail/<slug:slugInput>', views.detail_movie,name='detail_movie'),
    path('kategori/<slug:kategoriInput>', views.kategori_movie,name='kategori_movie'),
    path('', views.index, name='index'),
]