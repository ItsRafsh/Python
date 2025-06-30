from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Aktivitas
# Create your views here.
from django.contrib import messages

def index(request):
    aktifitas = Aktivitas.objects.all().order_by('-pupdate')
    kategori = Aktivitas.objects.values('Kategori__slug_kat','Kategori__nama').distinct()
    context = {
        'judul': 'Activities History',
        'heading': 'Selamat Datang di halaman Activitiessss',
        'aktifitase': aktifitas,
        'kategori': kategori,
    }
    return render(request, 'aktif/index.html', context)



def kategori_aktivitas(request,kategoriInput):
    aktivitas = Aktivitas.objects.filter(Kategori__slug_kat=kategoriInput).order_by('-pupdate')
    kategori = Aktivitas.objects.values('Kategori__slug_kat','Kategori__nama').distinct()
    context = {
        'judul': 'Kategori Aktivitas History',
        'heading':'halaman berdasarkan Kategori Aktivitas',
        'aktivitas_kat': aktivitas,
        'kategori': kategori,
    }
    return render(request, 'aktif/kategori.html', context)


def detail_aktivitas(request,slugInput):
    aktivitas = Aktivitas.objects.get(slug_ak=slugInput)
    context = {
        'judul': 'Detail Aktivitas History',
        'heading':'selamat datang di halaman Detail Aktivitas',
        'detail_aktivitas': aktivitas,
    }
    return render(request, 'aktif/detail.html', context)


# ---------------------- CRUD SYSTEM  ----------------------
@login_required(login_url='/')
def create_aktif(request):
    f_aktivitas = Aktivitasform(request.POST or None)
    if request.method == 'POST':
        if f_aktivitas.is_valid():
            aktivitas = f_aktivitas.save(commit=False)
            aktivitas.user = request.user
            aktivitas.save()
            messages.success(request, 'Data Berhasil Disimpan')
            return redirect('aktivitas:index')
    context = {
        'judul':'Create Blog',
        'f_aktivitas': f_aktivitas
    }
    return render(request, 'aktif/create.html', context)


@login_required
def update(request,up_slug):
    u_aktiv = get_object_or_404(Aktivitas, slug_ak=up_slug, user=request.user)  #itu slug_art ny field
    if request.method == 'POST':
        f_aktivitas = Aktivitasform(request.POST or None, instance=u_aktiv)
        if f_aktivitas.is_valid():
            f_aktivitas.save()
            return redirect('aktivitas:index')
    else:
        f_aktivitas = Aktivitasform(instance=u_aktiv)

    context = {
        'judul':'Update Blog',
        'f_aktivitas': f_aktivitas,
        'u_aktiv': u_aktiv
    }
    return render(request, 'aktif/update.html', context)

def delete(request,del_slug):
    del_aktivitas = get_object_or_404(Aktivitas, slug_ak=del_slug, user=request.user)
    del_aktivitas.delete()
    return redirect('aktivitas:index')

