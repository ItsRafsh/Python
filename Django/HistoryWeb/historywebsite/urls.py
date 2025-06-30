
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.index, name='index'),
    path("youtube/", include("youtube.urls", namespace="youtube")),
    path("movie/", include("movie.urls", namespace="movie")),
    path("aktivitas/", include("aktivitas.urls", namespace="aktivitas")),
    path("admin/", admin.site.urls),
]


