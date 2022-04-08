from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('user_not_in_time/', views.books_from_user, name='user_time'),
    path('all_users/', views.all_user, name='all_users'),
    path('all_users/<str:way>', views.all_user, name='all_users'),
    path('addUser/', views.add_user, name='add_user'),
    path('editUser/<id>', views.edit_user, name='edit_user')
]

#< ahref = "{% url 'user_time' %}"style = "color: cornflowerblue" > < li > < i class ="fas fa-envelope-open" > < / i > Users who does not hand over books on time < / li > < / a >