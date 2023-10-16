
from django.urls import path
from . import views

urlpatterns = [
    path('',views.product_store,name='store'),
    path('category/<slug:category_slug>/',views.product_store,name='product_by_store'),
    path('category/<slug:category_slug>/<slug:product_slug>/',views.product_details,name='product_detail'),
    path('search/', views.serch_products,name='search'),
    path('submit_reviews/<int:product_id>/',views.submit_reviews,name='submit_reviews'),



]