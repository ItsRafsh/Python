from django.shortcuts import render,redirect, get_object_or_404
from .models import Youtube
from .forms import Youtubeform
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required


def index(request,):
    youtube = Youtube.objects.all().order_by('-pupdate')
    category = Youtube.objects.values('Kategori__slug_kat','Kategori__nama').distinct()
    context = {
        'judul':'Youtube History',
        'heading':'selamat datang di halaman Youtubeee',
        'youtube': youtube,
        'categories': category,
    }
    return render(request, 'yt/index.html', context)

def detail_youtube(request, slugInput):
    youtube = Youtube.objects.get(slug_art=slugInput)
    context = {
        'judul':'Detail Youtube History',
        'heading':'selamat datang di halaman Detail Youtubeee',
        'detail_youtube': youtube,
    }
    return render(request, 'yt/detail.html', context)

def kategori_youtube(request,kategoriInput):  #kategoriInput tambah ini nanti
    youtube = Youtube.objects.filter(Kategori__slug_kat=kategoriInput).order_by('-pupdate')
    category = Youtube.objects.values('Kategori__slug_kat','Kategori__nama').distinct()
    context = {
        'judul':'Kategori Blog',
        'heading':'halaman berdasarkan Kategori Youtube',
        'categories': category,
        'youtube_kat': youtube,
    }
    return render(request, 'yt/kategori.html', context)




# ---------------------- CRUD SYSTEM  ----------------------
@login_required
def create_yt(request):
    f_youtube = Youtubeform(request.POST or None)
    if request.method == 'POST':
        if f_youtube.is_valid():
            youtube = f_youtube.save(commit=False)
            youtube.user = request.user
            youtube.save()
            messages.success(request, 'Data Berhasil Disimpan')
            return redirect('youtube:index')

    context = {
        'judul':'create Blog',
        'f_youtube': f_youtube
    }
    return render(request, 'yt/create.html', context)

@login_required
def update(request,del_slug):
    u_youtube = get_object_or_404(Youtube, slug_art=del_slug, user=request.user)  #itu slug_art ny field
    if request.method == 'POST':
        f_youtube = Youtubeform(request.POST or None, instance=u_youtube)
        if f_youtube.is_valid():
            f_youtube.save()
            return redirect('youtube:index')
    else:
        f_youtube = Youtubeform(instance=u_youtube)

    context = {
        'judul':'Update Blog',
        'f_youtube': f_youtube,
        'u_youtube': u_youtube
    }
    return render(request, 'yt/update.html', context)

@login_required
def delete(request,del_slug):
    youtube = get_object_or_404(Youtube, slug_art=del_slug, user=request.user)
    youtube.delete()
    return redirect('youtube:index')



# ---------------------- END CRUD SYSTEM  ----------------------





