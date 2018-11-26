from .views import cart_detail, cart_add, cart_remove
from django.urls import path
from django.conf.urls import url

app_name = 'cart'
urlpatterns = [
    path('', cart_detail, name='main'),
    url(r'^add/(?P<merchandise_id>[-\w\d]+)/$', cart_add, name='cart_add'),
    url(r'^remove/(?P<merchandise_id>[-\w\d]+)/$', cart_remove, name='cart_remove'),
]
