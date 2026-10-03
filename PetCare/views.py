from django.shortcuts import render


def index(request):
    return render(request, 'PetCare/index.html')


def services(request):
    return render(request, 'PetCare/services.html')


def tips(request):
    return render(request, 'PetCare/tips.html')


def contact(request):
    return render(request, 'PetCare/contact.html')