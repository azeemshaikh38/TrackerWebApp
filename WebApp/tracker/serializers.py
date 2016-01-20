from rest_framework import serializers
from tracker.models import Activities, Fields, Subfields

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = ('name', 'description')

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fields
        fields = ('name', 'description')

class SubfieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subfields
        fields = ('name', 'description', 'field')
