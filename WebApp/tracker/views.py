from django.shortcuts import render
from rest_framework import generics
from tracker.models import Activities, Fields, Subfields
from tracker.serializers import ActivitySerializer, FieldSerializer, SubfieldSerializer
# Create your views here.

class ActivityView(generics.ListCreateUpdateDestroyAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitySerializer

class FieldView(generics.ListCreateUpdateDestroyAPIView):
    queryset = Fields.objects.all()
    serializer_class = FieldSerializer

class SubfieldView(generics.ListCreateUpdateDestroyAPIView):
    queryset = Subfields.objects.all()
    serializer_class = SubfieldSerializer
  
