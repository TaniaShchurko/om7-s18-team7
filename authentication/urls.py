from django.urls import path
from . import views

app_name='user'
urlpatterns = [
    path('post/', views.user_post, name='add_user'),
    path('list/', views.user_list, name='user_list'),
    path('post/<int:id>', views.user_post, name='update_user'),

]
