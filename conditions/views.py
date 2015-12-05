
# Create your views here.
from rest_framework import viewsets
from conditions.models import Condition
from conditions.serializer import ConditionSerializer


class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
