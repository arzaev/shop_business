from django.db import models
from datetime import datetime

class Material(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.size


class Product(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    main_image = models.ImageField(null=True, blank=True, upload_to="images/")
    price = models.PositiveIntegerField()
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name


class ProductPhoto(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField("Image", upload_to="product_photos/")
    product = models.ForeignKey(Product, verbose_name="Product Photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    products = models.TextField()
    checked = models.BooleanField(default=False)
    code_order = models.CharField(max_length=200)
    client_ip = models.CharField(max_length=200, default='ip')
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()
    checked = models.BooleanField(default=False)
    client_ip = models.CharField(max_length=200, default='ip')
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
