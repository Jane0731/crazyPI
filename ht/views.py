from django.shortcuts import render
from .models import temperature_humidity
import datetime

def home(request):
    return render(request,'crazypi.html', locals())
