from django.urls import path
from . import views

urlpatterns = [path('users/', views.UserListCreateView.as_view(), name='create_list_user'),
               path('users/<int:pk>/', views.UserRetrieveUpdateDestroyView.as_view(), name='retrieve_update_destroy_user')]
