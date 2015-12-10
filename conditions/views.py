
# Create your views here.
from django.db import models
from conditions.models import Condition, Treatment
from django.http import HttpResponse

from conditions.serializer import ConditionSerializer, TreatmentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from rest_framework.parsers import JSONParser
import json

class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer

class TreatmentViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer

def index(request):
    json_data = open('/wt_challenge/data/aneurysm.json').read()
    return HttpResponse(json.dumps(json_data), content_type='conditions/json')
