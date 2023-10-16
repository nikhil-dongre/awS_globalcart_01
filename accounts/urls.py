from django.urls import path,include
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logut/',views.logout,name='logut'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('resetpassword_validate/<uidb64>/<token>/', views.reset_passoword_validate, name='resetpassword_validate'),
    path('forget_password/', views.forget_password, name='forget-password'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('order_details/<int:order_id>/',views.order_details,name='order_details')


]
