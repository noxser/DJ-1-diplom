from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from .models import OrderItem, Order
from cart.cart import Cart


# Create your views here.


@require_POST
def order_create(request):
    cart = Cart(request)
    if request.user.is_authenticated:
        order = Order.objects.create()
        order.user = request.user
        order.save()
        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     quantity=item['quantity'])
        # очистка корзины
        cart.clear()
        return redirect('cart:main')
    else:
        return render(request, 'account/login.html', {'err': 'Авторизуйтесь'})
