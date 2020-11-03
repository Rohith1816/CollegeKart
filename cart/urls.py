from django.urls import path
from cart.views import add_to_cart, remove_from_cart
app_name= 'mainapp'

urlpatterns = [
    path('cart/<slug>', add_to_cart, name='cart'),
    path('remove/<slug>', remove_from_cart, name='remove-cart'),
]