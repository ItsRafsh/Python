from django.shortcuts import render

# Create your views here.
def indexe(request):
    return render(request, 'kontak.html')