from rest_framework import serializers
from conditions.serializer import serializers

class TreatmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = 'conditions.Treatment'
        fields = ('id', 'condition', 'treatment_name', 'description', 'display_name',)

    def create(self, validated_data):
        return Treatment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.condition = validated_data.get('condition', instance.condition)
        instance.treatment_name = validated_data.get('treatment_name', instance.treatment_name)
        instance.description = validated_data.get('description', instance.description)
        instance.display_name = validated_data.get('display_name', instance.display_name)
        instance.save()
        return instance


class ConditionSerializer(serializers.HyperlinkedModelSerializer):
    treatments = TreatmentSerializer()
    class Meta:
        model = 'conditions.Treatment'
        fields = ('id', 'name', 'treatments',)

    def create(self, validated_data):
        return Condition.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
