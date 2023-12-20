from django.urls import path
from . import views

urlpatterns = [path('classes/', views.ClassListCreateView.as_view(), name='create-list-classes'),
               path('classes/<int:pk>/', views.ClassRetrieveUpdateDestroyView.as_view(),
                    name='retrieve-update-destroy-class'),
               path('series/', views.SeriesListCreateView.as_view(), name='create-list-series'),
               path('series/<int:pk>/', views.SeriesRetrieveUpdateDeleteView.as_view(), name='retrieve-update-series'),
               path('modalities/', views.ModalityListCreateView.as_view(), name='create-list-modalities'),
               path('modalities/<int:pk>/', views.ModalityRetrieveUpdateDeleteView.as_view(), name='retrieve-update-modality')]
