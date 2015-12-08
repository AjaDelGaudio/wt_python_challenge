
# Create your views here.
from django.db import models
from conditions.models import Condition, Treatment
from rest_framework import viewsets
from conditions.serializer import ConditionSerializer, TreatmentSerializer

class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer

class TreatmentViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
