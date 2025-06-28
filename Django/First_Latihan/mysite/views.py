from django.http import HttpResponse
from django.shortcuts import render


def index(rr):
    # ini ke 11
    context = {
        'judul': 'became pro ngoding',
        'dev': 'rafa boy'
    }
    return render(rr, 'index.html', context)





