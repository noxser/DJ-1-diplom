from .views import order_create
from django.urls import path

app_name = 'orders'
urlpatterns = [
    path('', order_create, name='order_create'),
]
