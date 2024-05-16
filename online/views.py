from random import choice, randint

from django.shortcuts import render, HttpResponse



# Create your views here.

def index(request):
    return render(request, 'online/index.html')


def bio(request):
    return render(request, 'online/bio.html')


def base(request):
    return render(request, 'online/base.html')


