from django.contrib import admin

from app.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['title', 'price', 'description']
#
# admin.site.register(Product)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['image', 'name']
