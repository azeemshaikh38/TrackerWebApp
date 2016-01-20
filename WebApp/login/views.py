from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from utilities.HttpResponses import HttpResponseError, HttpResponseSuccess

# Create your views here.

class LoginAPIView(APIView):
    def post(self, request):
        data = request.POST.dict()
        if 'username' not in data or 'password' not in data:
            return HttpResponseError("Username/Password is required", 400)
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            return HttpResponseError("Invalid username/password", 404)
        login(request, user)
        context = {}
        return redirect("home:home")

    def get(self, request):
        return render(request, 'login/login.html')
