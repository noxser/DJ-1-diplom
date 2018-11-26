from .views import product_list, product_detail
from django.conf.urls import url

app_name = 'shop'
urlpatterns = [
    url(r'^(?P<category_slug>[-\w]+)/$',
        product_list,
        name='product_list_by_category'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<merchandise_id>[-\w\d]+)$',
        product_detail,
        name='product_detail'),
]
