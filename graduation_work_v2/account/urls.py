from .views import login_in, logged_out
from django.urls import path

app_name = 'account'
urlpatterns = [
    path('', login_in, name='home'),
    path('logout/', logged_out, name='logged_out'),
]
