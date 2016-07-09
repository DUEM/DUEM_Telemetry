from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import motorstate, controlstate
import pickle
import json
import datetime

# Create your views here.

def controlsjson(request):
    controls_file = open("/dev/shm/controls","rb+")
    controls_status = pickle.load(controls_file)
    controls_status['time'] = controls_status['time'].isoformat() # json can't handle datetime objs
    data = json.dumps(controls_status)
    return HttpResponse(data)

def gpsjson(request):
    gps_file = open("/dev/shm/gps","rb+")
    gps_status = pickle.load(gps_file)
    data = json.dumps(gps_status)
    return HttpResponse(data)

def motorjson(request):
    motor_file = open("/dev/shm/motor","rb+")
    motor_status = pickle.load(motor_file)
    motor_status['time'] = motor_status['time'].isoformat() # json can't handle datetime objs
    data = json.dumps(motor_status)
    return HttpResponse(data)
