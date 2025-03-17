# demo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('art_archive/', views.art_archive, name='art_archive'),
    path('firstpick/', views.firstpick, name='firstpick'),
    path('ivrpov/', views.ivrpov, name='ivrpov'),
    path('comfortably_numb/', views.comfortably_numb, name='comfortably_numb'),
    path('bemyangel/', views.bemyangel, name='bemyangel'),
    path('brown_dreams/', views.brown_dreams, name='brown_dreams'),
    path('impressionism/', views.impressionism, name='impressionism'),
    path('realism/', views.realism, name='realism'),
    path('SIEVM/', views.SIEVM, name='SIEVM'),
    path('me?/', views.me, name='me?'),
    path('irony/', views.irony, name='irony'),
    path('about_me/', views.about_me, name='about_me'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.download, name='download'),

]
