from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from .models import OrderItem, Order
from cart.cart import Cart


# Create your views here.


@require_POST
def order_create(request):
    cart = Cart(request)

    order = Order.objects.create(
        username=request.user.username,
        first_name=request.user.first_name,
        last_name=request.user.last_name,
        email=request.user.email
    )
    for item in cart:
        OrderItem.objects.create(order=order,
                                 product=item['product'],
                                 quantity=item['quantity'])
    # очистка корзины
    cart.clear()
    return redirect('cart:main')
