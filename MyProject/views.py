from django.shortcuts import render
from django.http import HttpResponse

def produc_list(request):
    product = Product.objects.all()