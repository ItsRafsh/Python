from django.urls import path
from . import views


urlpatterns = [
    path('cari/', views.cari),  # ini urutan 9 kek nya
    path('artikel/', views.artikel),
    path('berita/', views.berita),
    path('', views.index),
]