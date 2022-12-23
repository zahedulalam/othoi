from django.urls import path
from . import views

urlpatterns = [
    path('product', views.product, name='product'),
    path('product_details', views.product_details, name='product_details'),
    path('order_details', views.order_details, name='order_details'),
]