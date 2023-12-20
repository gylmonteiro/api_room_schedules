from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Account
from .serializers import AccountSerializer


# Create your views here

class AccountListCreateView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
