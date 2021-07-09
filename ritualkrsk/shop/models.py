from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    main_image = models.ImageField(null=True, blank=True, upload_to="images/")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.category_name


class ProductSubCategory(models.Model):
    subcategory_name = models.CharField(max_length=255, unique=True)
    subcategory_slug = models.SlugField(max_length=255)
    category_name = models.ForeignKey(ProductCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = "Subcategory"

    def __str__(self):
        return self.subcategory_name