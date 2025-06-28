from django.shortcuts import render
from .models import Artikel
# Create your views here.


def index(request):
    article = Artikel.objects.all()
    category = Artikel.objects.values('Kategori__nama').distinct()
    context = {
        'judul':'Blog',
        'heading':'selamat datang di halaman Blogggg',
        'article': article,
        'categories': category,
    }
    return render(request, 'blog/index.html', context)

def detail_artikel(req, slugInput):
    detail_article = Artikel.objects.get(slug_art=slugInput)
    context = {
        'judul':'Detail Blog',
        'heading':'halaman Detail Bloggg',
        'detailArtikel': detail_article,
    }
    return render(req, 'blog/detail.html', context)




def kategori_artikel(request, kategoriInput):
    articles = Artikel.objects.filter(Kategori__nama=kategoriInput)
    category = Artikel.objects.values('Kategori__nama').distinct()
    context = {
        'judul':'Kategori Blog',
        'heading':'halaman berdasarkan Kategori Bloggg',
        'articles': articles,
        'categories': category,
    }
    return render(request, 'blog/kategori.html', context)
