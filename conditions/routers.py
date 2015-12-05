from conditions import route_handler
from conditions.route_handler import ModelRouter
from conditions.models import Condition, Treatment
from conditions.serializers import ConditionSerializer, TreatmentSerializer

class ConditionRouter(ModelRouter):
    route_name = 'condition'
    serializer_class = ConditionSerializer
    model = Conditiion

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.all()

class TreatmentRouter(ModelRouter):
    route_name = 'treatment'
    serializer_class = TreatmentSerializer
    model = Treatment

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.filter(condition_id=kwargs['treatment_id'])

route_handler.register(ConditionRouter)
route_handler.register(TreatmentRouter)
