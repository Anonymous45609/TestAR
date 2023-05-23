from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def combo(request):
    return render(request, 'main/combo.html')


def zacuski(request):
    return render(request, 'main/zacuski.html')


def desertu(request):
    return render(request, 'main/desertu.html')


def cup(request):
    return render(request, 'main/cup.html')


def kontaktu(request):
    return render(request, 'main/kontaktu.html')


def onas(request):
    return render(request, 'main/onas.html')


