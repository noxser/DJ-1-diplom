from django.shortcuts import render
from shop.models import Category
from .models import Article
from django.core.cache import cache


def main_page_articles(request):
    categories = cache.get_or_set('categories', Category.objects.all())
    sorted_article_list = Article.objects.all().filter(active_status=True).order_by('positions')
    return render(request, 'main_page.html', {
        'categories': categories,
        'articles': sorted_article_list
    })
