from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import Product, Category, User


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'amount']
    # fields = ['title', 'price', 'description']


#
# admin.site.register(Product)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'slug']
    fields = ['image', 'name']


admin.site.register(User, UserAdmin)
