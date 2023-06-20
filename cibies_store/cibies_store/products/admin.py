from django.contrib import admin
from cibies_store.products.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
