
from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.berita, name='berita'),
    path('tambah/', views.addBerita, name='tambah-berita'),
]