from django.contrib import admin
from .models import Product, ProductCategory, ProductSubCategory, ProductPhoto
from ritualkrsk import config

admin.site.site_header = "Shop admin"


class ProductPhotoInline(admin.StackedInline):
    model = ProductPhoto
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ("subcategories", )
    inlines = [ProductPhotoInline]


admin.site.register(ProductCategory)
admin.site.register(ProductSubCategory)
admin.site.register(ProductPhoto)