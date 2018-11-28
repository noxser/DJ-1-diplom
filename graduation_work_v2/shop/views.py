from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Review
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
    product = get_object_or_404(Product, merchandise_id=merchandise_id)
    categories = cache.get_or_set('categories', Category.objects.all())
    merchandise_id = product.merchandise_id
    print(request.session.get('has_commented_product', False))

    context = {'categories': categories,
               'category': product.category.name,
               'product': product
               }

    if request.session.get('has_commented_product', False):
        if str(merchandise_id) in request.session.get('has_commented_product'):
            context['can_review_add'] = False
        else:
            context['can_review_add'] = True
    else:
        context['can_review_add'] = True

    if request.POST:
        review_data = request.POST
        if request.POST.get('mark'):
            has_commented_product = request.session.get('has_commented_product', [])
            if merchandise_id not in has_commented_product:
                Review.objects.create(product=product,
                                      creator=review_data['name'],
                                      text=review_data['description'],
                                      rating=review_data['mark'])
                has_commented_product.append(str(merchandise_id))
                request.session['has_commented_product'] = has_commented_product
        else:
            context['err'] = {'info': 'Выберите рейтинг', 'creator': review_data['name'],
                              'text': review_data['description']}
        return redirect(product.get_absolute_url())

    context['reviews'] = Review.objects.filter(product=product).order_by('created')

    return render(request, 'shop/detail_view.html', context)
