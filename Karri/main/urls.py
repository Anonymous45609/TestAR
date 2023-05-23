from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('combo', views.combo, name='combo'),
    path('zacuski', views.zacuski, name='zacuski'),
    path('desertu', views.desertu, name='desertu'),
    path('cup', views.cup, name='cup'),
    path('kontaktu', views.kontaktu, name='kontaktu'),
    path('onas', views.onas, name='onas'),
]

