from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.orders,name='order')
    path('place_orders/',views.place_order ,name='place_order'), # type: ignore
    path('payments/',views.payments ,name='payments'), # type: ignore
    path('order_complete/',views.order_complete ,name='order_complete'), # type: ignore

]
