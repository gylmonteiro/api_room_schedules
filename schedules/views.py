from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import NotFound
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


class AllSchedulesForDateView(ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        date = self.kwargs['date']
        schedules_confirmed = Schedule.objects.filter(date=date)
        if schedules_confirmed.exists():
            return schedules_confirmed
        raise NotFound("Nenhum registro localizado")


class AllSchedulesForUserWithDateView(ListAPIView):
    serializer_class = ScheduleSerializer
    def get_queryset(self):
        date = self.kwargs['date']
        user_id = self.kwargs['user_id']
        print(date, user_id)
        schedules_confirmed = Schedule.objects.filter(date=date, responsible=user_id)
        if schedules_confirmed.exists():
            return schedules_confirmed
        raise NotFound("Nenhum registro localizado")