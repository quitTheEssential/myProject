from django.shortcuts import render
from .models import Products



def home(request):
    return render(request, 'store/home.html')

def about(request):
    return render(request, 'store/about.html', context = {'title': 'About'})

def shop(request):
    context = {

        'Products': Products.objects.all()
    }
    return render(request, 'store/shop.html', context = context)