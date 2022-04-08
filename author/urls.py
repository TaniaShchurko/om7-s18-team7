from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "author"

urlpatterns = [
    #path('books_by_id/', views.author_id_books, name='authors_books'),
    path('add_author/', views.add_author, name='add_author'),
    #path('books_by_authors_id/<id>', views.books_from_author, name='show_books')
    path('<id>/', views.books_from_author, name='books_from_author'),
    path('',views.addauthor, name='create_author' ),
    path('editAuthor/<id>', views.editauthor, name='edit_author'),
    path('authors', views.authors, name='allauthors'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

#<a href="{% url 'books_from_author' %}" style="color: cornflowerblue"><h1>Authors</h1></a> # to layout.html
