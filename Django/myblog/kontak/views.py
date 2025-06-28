from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from .forms import Kontakform
from .models import KontakModel

def index(request):
    contact = KontakModel.objects.all().order_by('-waktu_kirim')
    context = {
        'judul':'Kontak',
        'heading':'selamat datang di halaman Kontakkkkkk',
        'contact': contact,
    }
    return render(request, 'kontak/index.html', context)


def create(req):
    salah = None
    f_kontak = Kontakform(req.POST or None)
    if req.method == 'POST':
        if f_kontak.is_valid():
            f_kontak.save()
            return HttpResponseRedirect('/kontak/')
        else:
            salah = f_kontak.errors

    context = {
        'judul':'Kirim Pesan',
        'heading':'halaman Kirim Pesan',
        'f_kontak': f_kontak,
        'salah': salah,
    }
    return render(req, 'kontak/create.html', context)