from django.shortcuts import render
from rest_framework import generics
from tracker.models import Activities, Fields, ActivityFieldEffects
from tracker.serializers import ActivitySerializer, FieldSerializer, ActivityFieldEffectSerializer
# Create your views here.

class ActivityView(generics.ListCreateAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitySerializer

class FieldView(generics.ListCreateAPIView):
    queryset = Fields.objects.all()
    serializer_class = FieldSerializer

class ActivityFieldEffectView(generics.ListCreateAPIView):
    queryset = ActivityFieldEffects.objects.all()
    serializer_class = ActivityFieldEffectSerializer
