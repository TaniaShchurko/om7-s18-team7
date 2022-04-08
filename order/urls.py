from django.urls import path
from . import views

app_name='order'
urlpatterns = [
    path('', views.order_by_created_at, name='order_list'),
    path('sort_by_end', views.order_by_plated_end_at),
    path('user_<int:user_id>', views.order_from_specific_user, name='user_orders'),
    path('over_dated', views.over_dated_orders),
    path('post/', views.order_post, name='add_order'),
    path('post/<int:id>', views.order_post, name='update_order'),

]

