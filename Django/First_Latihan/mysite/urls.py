# from . views import index, blog     #cara panggil file views nya
from . import views                 # di setiap fungsi kasi views.index gitu\
from django.contrib import admin
from django.urls import path, include


# from . views import *                 # langsung smua function

urlpatterns = [
    path('', views.index),
    path('blog/', include('blog.urls')),
    path('kontak/', include('kontak.urls')),
    path("admin/", admin.site.urls),
]
