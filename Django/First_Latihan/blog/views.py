from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    context = {
        'judul': 'became pro networking',
        'dev': 'hariss boy',
        'nav': [
            ['/','Home'],
            ['/blog','Blog'],
            ['/blog/artikel','Artikel'],
            ['/blog/berita','Berita'],
        ]
    }
    # return render(request, 'blog.html')
    return render(request, 'blog/index.html', context)





def cari(request):
    # return HttpResponse('<h1> gata ini cari </h1>')
    return render(request, 'cari.html')



# ini yg ke 11
def artikel(request):
    context = {
        'judul': 'artikel meledek',
        'dev': 'artikell rafa boy'
    }
    return render(request, 'blog/index.html', context)


def berita(request):
    context = {
        'judul': 'berita duarrr',
        'dev': 'berita hariss boy'
    }
    return render(request, 'blog/index.html', context)









