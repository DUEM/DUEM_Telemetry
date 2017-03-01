from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django.core import serializers
from .models import motorstate, controlstate
import csv
import datetime
import json

class Echo(object):
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value

# Create your views here.

def controlsjson(request):
    controls_file = open("/dev/shm/controls","r+")
    controls_status = json.load(controls_file)
    data = json.dumps(controls_status)
    return HttpResponse(data)

def gpsjson(request):
    gps_file = open("/dev/shm/gps","r+")
    gps_status = json.load(gps_file)
    data = json.dumps(gps_status)
    return HttpResponse(data)

def motorjson(request):
    motor_file = open("/dev/shm/motor","r+")
    motor_status = json.load(motor_file)
    data = json.dumps(motor_status)
    return HttpResponse(data)

def csvout(request):
    """A view that streams a large CSV file."""
    # Generate a sequence of rows. The range is based on the maximum number of
    # rows that can be handled by a single sheet in most spreadsheet
    # applications.
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse((writer.writerow(row) for row in motorstate.objects.all()),
                                     content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="motor.csv"'
    return response
