from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('user_not_in_time/', views.books_from_user, name='user_time'),
    path('all_users/', views.all_user, name='all_users'),
    path('all_users/<str:way>', views.all_user, name='all_users'),
    path('addUser/', views.add_user, name='add_user'),
    path('editUser/<id>', views.edit_user, name='edit_user'),
    path('create/', views.UserCreateView.as_view(), name='rest_add_user'),
    path('list/', views.UserListView.as_view(), name='rest_all_users'),
    path('detail/<int:pk>/', views.UserDetailView.as_view(), name='rest_edit_user'),
    path('<int:user_id>/order/<int:pk>', views.UserOrderDetailView.as_view(), name='rest_user_order'),
    
]

#< ahref = "{% url 'user_time' %}"style = "color: cornflowerblue" > < li > < i class ="fas fa-envelope-open" > < / i > Users who does not hand over books on time < / li > < / a >