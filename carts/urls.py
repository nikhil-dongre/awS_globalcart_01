from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.cart ,name='cart'),
    path('add_cart/<int:product_id>/',views.add_cart ,name='add_cart'),
    path('remove/<int:product_id>/<int:cart_item_id>/',views.remove_cart ,name='remove_cart'),
    path('remove_whole_product/<int:product_id>/<int:cart_item_id>/',views.remove_all_cart_items ,name='remove_whole_product'),
    path('checkout/',views.checkout ,name='checkout'),



]
