from django.contrib import admin

from .models import Product, ProductCategory, ProductSubCategory

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductSubCategory)