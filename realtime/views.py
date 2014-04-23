from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import motorstate

def motorjson(request):
    data = serializers.serialize("json",[motorstate.objects.latest(),])
    return HttpResponse(data)
# Create your views here.
