from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('books/', views.books, name='books'),
    path('<id>/', views.book_by_id, name='book_by_id'),
    path('books/byname/desc', views.books_name_desc, name='books_name_desc'),
    path('books/bycount', views.books_count, name='books_count'),
    path('books/unordered', views.unordered, name='unordered'),
    path('books/addbook', views.addbook, name='addbook'),
    path('<id>/editbook', views.edit, name='edit_book'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
