from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import RulesSerializer
from .models import Rules
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rules.permissions import IsOwnerOrReadOnly

class RulesList(ListCreateAPIView):
    #IsAuthenticatedOrReadOnly is from rest_framework permissions
    permission_classes = (IsAuthenticatedOrReadOnly,) 
    queryset = Rules.objects.all()
    serializer_class = RulesSerializer


class RulesDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Rules.objects.all()
    serializer_class = RulesSerializer


