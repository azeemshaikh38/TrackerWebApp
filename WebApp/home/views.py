from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from tracker.models import Activities, Fields, UserFields, ActivityFieldEffects
import json
# Create your views here.

@login_required
def home(request):
    context = {}
    context["userfields"] = UserFields.objects.filter(user=request.user)
    context["useractivities"] = ActivityFieldEffects.objects.filter(field_id__in=context["userfields"].values_list('field_id', flat=True))
    return render(request, 'home/home.html', context=context)

@login_required
def choose_fields(request):
    context = {}
    context["fields"] = Fields.objects.all().exclude(id__in=UserFields.objects.filter(user=request.user).values_list('field_id', flat=True)).filter(subfieldOf__isnull=True)
    return render(request, 'home/choose_fields.html', context=context)

@login_required
def submit_fields(request):
    post_data = request.POST.dict()
    for k, v in post_data.iteritems():
        if v == "true":
            u = UserFields(user=request.user, field_id=k, score=1)
            u.save()
    return redirect("home:home")
