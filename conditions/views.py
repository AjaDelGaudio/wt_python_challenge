
# Create your views here.
from rest_framework import viewsets
from conditions.serializer import ConditionSerializer, TreatmentSerializer
from conditions.models import Condition, Treatment


class ConditionViewSet(conditions.ViewSetCreatAPIView):
    queryset = Condition.objects.all()
    serializer = ConditionSerializer

class TreatmentViewSet(conditions.ViewSetCreateAPIView):
    queryset = Treatment.objects.all()
    serializer = TreatmentSerializer


