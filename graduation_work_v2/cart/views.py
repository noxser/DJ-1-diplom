from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product, Category
from .cart import Cart
from django.core.cache import cache


# Create your views here.


def cart_detail(request):
    cart = Cart(request)
    quantity = len(request.session.get('cart'))
    categories = cache.get_or_set('categories', Category.objects.all())
    return render(request, 'cart/cart.html',
                  {'cart': cart,
                   'quantity': quantity,
                   'categories': categories
                   })


# отработает только при POST запросе
@require_POST
def cart_add(request, merchandise_id):
    cart = Cart(request)
    product = get_object_or_404(Product, merchandise_id=merchandise_id)
    cart.add(product=product)
    # перенаправляем на предыдущюю страничку
    # коряво как я понял но пока так )))
    referer = request.META.get('HTTP_REFERER', None)
    if referer:
        return HttpResponseRedirect(referer)
    else:
        return redirect('index')


def cart_remove(request, merchandise_id):
    cart = Cart(request)
    product = get_object_or_404(Product, merchandise_id=merchandise_id)
    cart.remove(product)
    return redirect('cart:main')
