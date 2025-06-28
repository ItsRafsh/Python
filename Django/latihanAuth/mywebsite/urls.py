
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import *
from django.urls import path, include

urlpatterns = [
    path('', index),
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path("admin/", admin.site.urls),
]


