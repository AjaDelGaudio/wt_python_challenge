
# Create your views here.
from rest_framework import viewsets
from conditions.models import Condition, Treatment
from conditions.serializer import ConditionSerializer, TreatmentSerializer


class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer

class TreatmentViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
