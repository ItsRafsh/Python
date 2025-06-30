
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'youtube'
urlpatterns = [
    # path('login/', views.login, name='login'),
    path('update/<slug:del_slug>/', views.update, name='update'),
    path('delete/<slug:del_slug>/', views.delete, name='delete'),
    path('create/', views.create_yt, name='create_yt'),
    path('detail/<slug:slugInput>', views.detail_youtube,name='detail_youtube'),
    path('kategori/<slug:kategoriInput>', views.kategori_youtube,name='kategori_youtube'),
    path('', views.index, name='index'),
]

#update dan delete punya slug yg sama itu gpp, asal link ny beda