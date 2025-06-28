from django.shortcuts import render

def index(req):
    context = {
        'judul':'home',
        'heading':'selamat datang di halaman home',
    }
    return render(req, 'index.html', context)
