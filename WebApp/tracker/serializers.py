from rest_framework import serializers
from tracker.models import Activities, Fields, ActivityFieldEffects

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = ('name', 'description')

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fields
        fields = ('name', 'description', 'subfieldOf')

class ActivityFieldEffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityFieldEffects
        field = ('activity', 'field', 'effect')
