from django.contrib import admin

# Register your models here.

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category',)

    search_fields = ('name', )

    list_filter = ('category',)

    

admin.site.register(Product,ProductAdmin)