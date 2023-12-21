from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Schedule, Place, Time
from .serializers import PlaceSerializer, TimeSerializer, ScheduleSerializer


class PlaceListCreateView(ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class TimeListCreateView(ListCreateAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer


class TimeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer


class ScheduleListCreateView(ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
