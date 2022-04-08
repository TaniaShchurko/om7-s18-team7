from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.orders, name='orders'),
    path('addOrder/', views.addOrder, name='addOrder'),
    path('db/', views.db, name='db'),
    path('editOrder/<id>', views.editOrder, name='editOrder')
]
