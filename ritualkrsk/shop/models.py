from django.db import models


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


class Product(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    main_image = models.ImageField(null=True, blank=True, upload_to="images/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pub_date = models.DateTimeField('date published')
    category = models.ForeignKey(ProductCategory, verbose_name="Category", on_delete=models.CASCADE)
    subcategories = models.ManyToManyField(ProductSubCategory, verbose_name="subcategories")

    def __str__(self):
        return self.name


class ProductPhoto(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField("Image", upload_to="product_photos/")
    product = models.ForeignKey(Product, verbose_name="Product Photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.name



