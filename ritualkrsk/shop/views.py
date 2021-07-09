from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product, ProductCategory
from ritualkrsk import config

number_of_products_on_page = 6


def home_page(request, page='page', page_number=1):
    products = list(reversed(Product.objects.all()))
    try:
        current_page = Paginator(products, number_of_products_on_page)
    except ObjectDoesNotExist:
        current_page = Paginator(products, number_of_products_on_page)

    context = {}
    context['categories'] = ProductCategory.objects.all()
    context['title_shop'] = config.TITLE_SHOP
    context['pages'] = current_page.page(page_number)

    return render(request, 'home.html', context)


def contacts(request):
    context = {}
    return render(request, 'contacts.html', context)