from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.orders, name='orders'),
    path('addOrder/', views.addOrder, name='addOrder'),
    path('db/', views.db, name='db'),
    path('editOrder/<id>', views.editOrder, name='editOrder'),
    path('list/', views.OrderListView.as_view(), name='rest_all_users'),
    path('create/', views.OrderCreateView.as_view(), name='rest_add_order'),
    
]
