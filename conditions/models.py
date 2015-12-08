from django.db import models
from conditions.serializer import ConditionSerializer, TreatmentSerializer 
# Create your models here.

class Condition(models.Model):
    serializer_class = ConditionSerializer
    name = models.CharField(max_length=256, blank=False, help_text="name of condition")

    def __str__(self):
        return self.condition_text

    class Meta(object):
        verbose_name = "Condition"
        verbose_name_plural = "Conditions"

class Treatment(models.Model):
    serializer_class = TreatmentSerializer
    condition = models.ForeignKey(Condition)
    treatment_name = models.CharField(max_length=256, blank=False, help_text="name of treatment")
    description = models.CharField(max_length=500, help_text="description of treatment")
    display_name = models.CharField(max_length=256, help_text="brief name of treatment for display")

    def __str__(self):
        return self.treatment_text
