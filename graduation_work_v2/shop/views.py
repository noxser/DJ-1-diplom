from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache import cache


# Create your views here.

def product_list(request, category_slug):
    categories = cache.get_or_set('categories', Category.objects.all())
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.all().filter(category=category)
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # если page не число показываем первую
        products = paginator.page(1)
    except EmptyPage:
        # если page выходит за диапазон показываем последнюю
        products = paginator.page(paginator.num_pages)

    return render(request,
                  'shop/list_view.html',
                  {'category': category.name,
                   'categories': categories,
                   'product_list': products,
                   })


def product_detail(request, merchandise_id, category_slug):
    product = get_object_or_404(Product,
                                merchandise_id=merchandise_id,
                                )
    categories = cache.get_or_set('categories', Category.objects.all())
    return render(request,
                  'shop/detail_view.html',
                  {'categories': categories,
                   'category': product.category.name,
                   'product': product})
