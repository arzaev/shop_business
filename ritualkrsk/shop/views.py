
from django.shortcuts import render
from .models import Product, ProductCategory
from ritualkrsk import config


def home_page(request):
    context = {}
    context['products'] = Product.objects.all()
    context['categories'] = ProductCategory.objects.all()
    context['title_shop'] = config.TITLE_SHOP
    return render(request, 'home.html', context)


def contacts(request):
    context = {}
    return render(request, 'contacts.html', context)