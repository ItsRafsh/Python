from django.urls import path
from . import views

app_name = 'aktivitas'

urlpatterns = [
    path('update/<slug:up_slug>/', views.update, name='update'),
    path('delete/<slug:del_slug>/', views.delete, name='delete'),
    path('create/', views.create_aktif, name='create_aktif'),
    path('detail/<slug:slugInput>', views.detail_aktivitas,name='detail_aktivitas'),
    path('kategori/<slug:kategoriInput>', views.kategori_aktivitas,name='kategori_aktivitas'),
    path('', views.index, name='index'),
]
