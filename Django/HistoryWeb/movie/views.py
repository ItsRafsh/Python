from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required


def index(request):
    movie = Movie.objects.all().order_by('-pupdate')
    kategori = Movie.objects.values('Kategori__slug_kat','Kategori__nama').distinct()
    context = {
        'judul': 'Movie History',
        'heading':'selamat datang di halaman Movie',
        'movies': movie,
        'kategori': kategori,
    }
    return render(request, 'mv/index.html', context)


def detail_movie(request, slugInput):
    movie = Movie.objects.get(slug_mv=slugInput)
    context = {
        'judul': 'Detail Movie History',
        'heading':'selamat datang di halaman Detail Movie',
        'detail_movie': movie,
    }
    return render(request, 'mv/detail.html', context)


def kategori_movie(request,kategoriInput):
    movie = Movie.objects.filter(Kategori__slug_kat=kategoriInput).order_by('-pupdate')
    kategori = Movie.objects.values('Kategori__slug_kat','Kategori__nama').distinct()
    context = {
        'judul': 'Kategori Movie Hisotry',
        'heading':'halaman berdasarkan Kategori Movie',
        'movie_kat': movie,
        'kategori': kategori,
    }
    return render(request, 'mv/kategori.html', context)



# ---------------------- CRUD SYSTEM  ----------------------
@login_required(login_url='/')
def create_mv(request):
    f_movie = Movieform(request.POST or None)
    if request.method == 'POST':
        if f_movie.is_valid():
            movie = f_movie.save(commit=False)
            movie.user = request.user
            movie.save()
            messages.success(request, 'Data Berhasil Disimpan')
            return redirect('movie:index')
    context = {
        'judul':'create Blog',
        'f_movie': f_movie
    }
    return render(request, 'mv/create.html', context)


@login_required
def update(request,up_slug):
    u_movie = get_object_or_404(Movie, slug_mv=up_slug, user=request.user)  #itu slug_art ny field
    if request.method == 'POST':
        f_movie = Movieform(request.POST or None, instance=u_movie)
        if f_movie.is_valid():
            f_movie.save()
            return redirect('movie:index')
    else:
        f_movie = Movieform(instance=u_movie)

    context = {
        'judul':'Update Blog',
        'f_movie': f_movie,
        'u_movie': u_movie
    }
    return render(request, 'mv/update.html', context)

def delete(request,del_slug):
    del_movie = get_object_or_404(Movie, slug_mv=del_slug, user=request.user)
    del_movie.delete()
    return redirect('movie:index')















