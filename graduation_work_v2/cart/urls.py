from .views import cart_detail, cart_add, cart_remove
from django.urls import path

app_name = 'cart'
urlpatterns = [
    path('', cart_detail, name='main'),
    path('add/(<merchandise_id>[-\w\d]+)/', cart_add, name='cart_add'),
    path('remove/(<merchandise_id>[-\w\d]+)/', cart_remove, name='cart_remove'),
]
