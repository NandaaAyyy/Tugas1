from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 


# Create your views here.


def berita(request):
    return render(request, 'berita.html')


def addBerita(request):
    return render(request, 'tambahBerita.html')
