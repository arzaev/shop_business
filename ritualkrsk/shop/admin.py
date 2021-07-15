from django.contrib import admin
from .models import Product, ProductPhoto, Material, Size, Order, Question
from ritualkrsk import config

admin.site.site_header = "Shop admin"


class ProductPhotoInline(admin.StackedInline):
    model = ProductPhoto
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductPhotoInline]


class OrderAdmin(admin.ModelAdmin):
    list_display = ("email", "code_order", "date", "checked")


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "date", "checked")


admin.site.register(ProductPhoto)
admin.site.register(Material)
admin.site.register(Size)
admin.site.register(Order, OrderAdmin)
admin.site.register(Question, QuestionAdmin)