from django.contrib import admin
from .models import Article, ArticleItem


# Register your models here.


class ArticleItemInline(admin.TabularInline):
    model = ArticleItem
    raw_id_fields = ['product']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'positions', 'title', 'created', 'active_status']
    list_filter = ['id', 'active_status']
    list_editable = ['active_status']
    inlines = [ArticleItemInline]


admin.site.register(Article, ArticleAdmin)
