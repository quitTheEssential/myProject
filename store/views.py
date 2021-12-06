from django.shortcuts import render
from .models import Products
posts = [
    {
        'author': 'Robert',
        'title': 'AirMax97',
        'content': 'New brand AirMax97',
        'date_posted': 'November 07, 2021'
    },
    {
        'author': 'Jarek',
        'title': 'AirMax95',
        'content': 'New brand AirMax95',
        'date_posted': 'November 08, 2021'
    }
]


def home(request):
    return render(request, 'store/home.html')

def about(request):
    return render(request, 'store/about.html', context = {'title': 'About'})

def shop(request):
    context = {
        'posts':posts
        # 'Products': Products.objects.all()
    }
    return render(request, 'store/shop.html', context = context)