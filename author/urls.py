from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "author"

urlpatterns = [
    path('add_author/', views.add_author, name='add_author'),
    path('',views.addauthor, name='create_author' ),
    path('editAuthor/<id>', views.editauthor, name='edit_author'),
    path('authors', views.authors, name='allauthors'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('create/', views.AuthorCreateView.as_view(), name='rest_add_author'),
    path('list/', views.AuthorListView.as_view(), name='author-detail'),
    path('detail/<int:pk>/', views.AuthorDetailView.as_view(), name='rest_edit_author'),

]

#<a href="{% url 'books_from_author' %}" style="color: cornflowerblue"><h1>Authors</h1></a> # to layout.html
