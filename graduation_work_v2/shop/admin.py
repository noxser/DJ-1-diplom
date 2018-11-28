from django.contrib import admin
from .models import Category, Product, Review


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'merchandise_id']
    list_filter = ['category', 'name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 15  # товаров на одной странице


admin.site.register(Product, ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'creator', 'created', 'rating']


admin.site.register(Review, ReviewAdmin)
