from django.urls import path
from . import views

urlpatterns = [
    path('', views.authors_update),
    path('<int:id>', views.authors_update, name='update_author'),
    path('list', views.author_list),
    
]
