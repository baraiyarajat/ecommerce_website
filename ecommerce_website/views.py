from django.shortcuts import render
from store.models import Product


def home(request):
    # Get all products to display on Home Page
    products = Product.objects.all().filter(is_available=True)
    context = {'products': products}

    return render(request, 'home.html', context)
