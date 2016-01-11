from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
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
        return HttpResponseSuccess("Authenticated!")

    def get(self, request):
        return HttpResponse(render(request, 'login/login.html'))
        #return HttpResponseSuccess("You will see login page here")
