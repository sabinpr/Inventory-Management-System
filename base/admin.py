from django.contrib import admin
from .models import Product, ProductType, Department, Vendor, Purchase, Sell, User

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(Department)
admin.site.register(Vendor)
admin.site.register(Purchase)
admin.site.register(Sell)
