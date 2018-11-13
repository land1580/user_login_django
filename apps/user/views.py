from django.shortcuts import render, HttpResponse
from apps.user.models import User

# Create your views here.

def index(request):
    response = User.objects.all()
    return HttpResponse(response)