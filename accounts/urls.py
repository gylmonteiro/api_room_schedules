from django.urls import path
from . import views

urlpatterns = [path('accounts/', views.AccountListCreateView.as_view(), name='create_list_account'),
               path('accounts/<int:pk>/', views.AccountRetrieveUpdateDestroy.as_view(), name='retrieve_update_delete_account'),
               ]
