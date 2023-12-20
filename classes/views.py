from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Class, Series, Modality
from .serializers import ClassSerializer, SeriesSerializer, ModalitySerializer


# Create your views here.
# Views for Classes
class ClassListCreateView(ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


# finish views to Classes

# Views Series

class SeriesListCreateView(ListCreateAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer


class SeriesRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer


# finish views to Series

# Views to Modality

class ModalityListCreateView(ListCreateAPIView):
    queryset = Modality.objects.all()
    serializer_class = ModalitySerializer


class ModalityRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Modality.objects.all()
    serializer_class = ModalitySerializer
