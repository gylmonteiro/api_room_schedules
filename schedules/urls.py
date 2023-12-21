from django.urls import path
from . import views

urlpatterns = [path('times/', views.TimeListCreateView.as_view(), name='list-create-time'),
               path('times/<int:pk>/', views.TimeRetrieveUpdateDestroyView.as_view(), name='retrieve-update-destroy-time'),
               path('places/', views.PlaceListCreateView.as_view(), name='list-create-places'),
               path('places/<int:pk>/', views.PlaceRetrieveUpdateDestroyView.as_view(), name='retrieve-update-destroy-place'),
               path('schedules/', views.ScheduleListCreateView.as_view(), name='list-create-schedules'),
               path('schedules/<int:pk>/', views.ScheduleRetrieveUpdateDestroyView.as_view(), name='retrieve-update-destroy-schedule')]