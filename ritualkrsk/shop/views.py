from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from .models import Product, ProductCategory
from ritualkrsk import config
from django.views.generic.base import View
from django.views.generic import ListView, DetailView


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
        # context['categories'] = ProductCategory.objects.all()
        context['title_shop'] = config.TITLE_SHOP
        return context


class FilterProductListView(CategoriesSubCategories, ListView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 1

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
        context['title_shop'] = config.TITLE_SHOP
        context["category"] = ''.join([f"category={x}&" for x in self.request.GET.getlist("category")])
        context["subcategory"] = ''.join([f"subcategory={x}&" for x in self.request.GET.getlist("subcategory")])
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_shop'] = config.TITLE_SHOP
        return context
