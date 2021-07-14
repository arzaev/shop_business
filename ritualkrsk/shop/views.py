
from django.db.models import Q
from django.http import HttpResponse
from .models import Product, ProductCategory
from ritualkrsk import config
from django.views.generic import ListView, DetailView
import json
from .cart import Cart, cart_html


class CategoriesSubCategories:

    def get_categories(self):
        return ProductCategory.objects.all()

    def get_subcategories(self):
        return CategoriesSubCategories.objects.all()


class ProductListView(CategoriesSubCategories, ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = "product_list.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cart = cart_html(self.request)
        context['cart'] = cart[0]
        context['general_price'] = cart[1]

        context['MD_LIST_PRODUCTS'] = config.MD_LIST_PRODUCTS
        context['BG_COLOR'] = config.BG_COLOR
        context['title_shop'] = config.TITLE_SHOP
        return context


class FilterProductListView(CategoriesSubCategories, ListView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 6

    def get_queryset(self):
        if len(self.request.GET.getlist("subcategory")) == 0:
            queryset = Product.objects.filter(
                Q(category__in=self.request.GET.getlist("category")) |
                Q(subcategories__in=self.request.GET.getlist("subcategory"))
            ).distinct()
            return queryset
        else:
            queryset = Product.objects.filter(
                Q(category__in=self.request.GET.getlist("category")),
                Q(subcategories__in=self.request.GET.getlist("subcategory"))
            ).distinct()
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['MD_LIST_PRODUCTS'] = config.MD_LIST_PRODUCTS
        context['BG_COLOR'] = config.BG_COLOR
        context['title_shop'] = config.TITLE_SHOP

        cart = cart_html(self.request)
        context['cart'] = cart[0]
        context['general_price'] = cart[1]

        context["category"] = ''.join([f"category={x}&" for x in self.request.GET.getlist("category")])
        context["subcategory"] = ''.join([f"subcategory={x}&" for x in self.request.GET.getlist("subcategory")])
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"

    def get_context_data(self, **kwargs):
        Cart(self.request)
        context = super().get_context_data(**kwargs)

        cart = cart_html(self.request)
        context['cart'] = cart[0]
        context['general_price'] = cart[1]

        context['MD_LIST_PRODUCTS'] = config.MD_LIST_PRODUCTS
        context['BG_COLOR'] = config.BG_COLOR
        context['title_shop'] = config.TITLE_SHOP
        return context


def add_product_to_cart(request):
    if request.is_ajax():
        data = json.loads(request.body.decode('utf-8'))
        Cart(request).add_product(data)
    return HttpResponse()


def remove_product_from_cart(request):
    if request.is_ajax():
        data = json.loads(request.body.decode('utf-8'))
        Cart(request).remove_product(data)
    return HttpResponse()