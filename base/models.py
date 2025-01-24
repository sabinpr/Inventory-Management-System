from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    department = models.ManyToManyField(Department)
    description = models.TextField()

    def __str__(self):
        return self.name


class Purchase(models.Model):
    price = models.FloatField()
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase of {self.product.name} from {self.vendor.name}"


class Sell(models.Model):
    price = models.FloatField()
    quantity = models.IntegerField()
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale of {self.Product.name} to {self.customer_name}"
