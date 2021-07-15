import decimal

from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import View

from .models import Product, Material, Size
from ritualkrsk import config
from django.views.generic import ListView, DetailView
import json
from .cart import Cart, cart_html
from decimal import Decimal as D


class MaterialSizePrice:
    def get_material(self):
        return Material.objects.all()

    def get_size(self):
        return Size.objects.all()

    # def get_price(self):
    #     return Product.objects.filter(price__range=(price1, price2))


class ProductListView(MaterialSizePrice, ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = "product_list.html"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        Cart(self.request)
        cart = cart_html(self.request)
        context['cart'] = cart[0]
        context['general_price'] = cart[1]

        context['MD_LIST_PRODUCTS'] = config.MD_LIST_PRODUCTS
        context['BG_COLOR'] = config.BG_COLOR
        context['title_shop'] = config.TITLE_SHOP
        return context


class FilterProductListView(MaterialSizePrice, ListView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 9

    def get_queryset(self):
        material = self.request.GET.getlist("material")
        self.material = material
        if len(material) == 0:
            m = Material.objects.all()
            for i in m:
                material.append(str(i.id))
        size = self.request.GET.getlist("size")
        self.size = size
        if len(size) == 0:
            s = Size.objects.all()
            for i in s:
                size.append(str(i.id))

        try:
            price1 = int(self.request.GET.get('min_filter_price', 0))
            price2 = int(self.request.GET.get('max_filter_price', 0))
        except ValueError:
            price1 = 0
            price2 = 9999999

        self.price1 = price1
        self.price2 = price2

        queryset = (
            Product.objects.filter(
                material__in=material,
                size__in=size,
                price__range=(price1, price2)
            )).distinct()
        return queryset

        # if len(material) == 0 and len(size) == 0:
        #
        #     queryset = (
        #         Product.objects.filter(price__range=(price1, price2))).distinct()
        #     return queryset
        # if len(material) == 0:
        #     queryset = (
        #         Product.objects.filter(size__in=self.request.GET.getlist("size"),
        #                                price__range=(price1, price2))).distinct()
        #     return queryset
        # if len(size) == 0:
        #     queryset = (
        #         Product.objects.filter(material__in=self.request.GET.getlist("material"),
        #                                price__range=(price1, price2))).distinct()
        #     return queryset
        # else:
        #     queryset = (
        #         Product.objects.filter(size__in=self.request.GET.getlist("size"),
        #                                material__in=self.request.GET.getlist("material"),
        #                                price__range=(price1, price2)
        #                                )
        #                             ).distinct()
        #     return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['MD_LIST_PRODUCTS'] = config.MD_LIST_PRODUCTS
        context['BG_COLOR'] = config.BG_COLOR
        context['title_shop'] = config.TITLE_SHOP

        cart = cart_html(self.request)
        context['cart'] = cart[0]
        context['general_price'] = cart[1]

        context["material"] = ''.join([f"material={x}&" for x in self.request.GET.getlist("material")])
        context["size"] = ''.join([f"size={x}&" for x in self.request.GET.getlist("size")])

        context["min_filter_price"] = "min_filter_price=" + self.request.GET.getlist("min_filter_price")[0] + "&"
        context["max_filter_price"] = "max_filter_price=" + self.request.GET.getlist("max_filter_price")[0] + "&"

        context["list_mat"] = self.material
        context["list_size"] = self.size

        context["price1"] = self.price1
        context["price2"] = self.price2
        return context


class ProductDetailView(MaterialSizePrice, DetailView):
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

        pr = Product.objects.get(id=self.kwargs.get('pk'))

        products = Product.objects.filter(material__in=[pr.material_id])[:8]
        context['similarProducts'] = products

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


def update_product_in_cart(request):
    if request.is_ajax():
        data = json.loads(request.body.decode('utf-8'))
        Cart(request).update_product(data)
    return HttpResponse()


class CartListView(ListView):
    model = Product
    template_name = "cart.html"

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


class CheckoutListView(ListView):
    model = Product
    template_name = "checkout.html"

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