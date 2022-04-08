from django.urls import path
from . import views


app_name = 'book'
urlpatterns = [
    path('', views.index),
    path('book/', views.all_books),
    path('book/<int:id_book>/', views.book_by_id, name='book_by_id'),
    path('book/author_<int:author_id>/', views.filter_by_author_id),
    path('book/name_<part_of_name>/', views.filter_by_part_of_name),
    path('book/sort_name_asc/', views.sort_by_name_asc),
    path('book/sort_name_desc/', views.sort_by_name_desc),
    path('book/sort_by_count/', views.sort_by_count),
    path('book/unordered/', views.all_unordered_books),
    path('book/post/', views.book_post, name='book_add'),
    path('book/post/<int:id>', views.book_post, name='book_update'),
    
]
