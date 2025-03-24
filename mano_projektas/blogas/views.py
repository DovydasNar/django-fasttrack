from django.shortcuts import render
from django.http import HttpResponse

def kontaktai(request):
    return HttpResponse('Susisiekite su mumis!')


def naujienos(request):
    kontekstas = {
        'pavadinimas': 'Naujienos',
        'antraste': 'Svieziausios naujienos'
    }
    return render(request, 'naujienos.html', kontekstas)

def apie(request):
    kontekstas = {
        'pavadinimas': 'Apie mus',
        'antraste': 'Apie mus'
    }
    return render(request, 'apie.html', kontekstas)

def autorius(request):
    kontekstas = {
        'vardas': 'Dovydas',
        'pomegiai': ['Programavimas', 'Sportas', 'Motociklai', 'Zvejyba']
    }
    return render(request, 'autorius.html', kontekstas)


def home(request):
    return HttpResponse('Cia yra pagrindinis Django puslapis!')
