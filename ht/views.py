from django.shortcuts import render
from .models import temperature_humidity
import datetime

def home(request):
    last_one = temperature_humidity.objects.last()
    last= temperature_humidity.objects.all().order_by('-id')[:6]
    last_six = last[1]
    last_five = last[2]
    last_four = last[3]
    last_three = last[4]
    last_two =last[5]

    return render(request,'crazypi.html', locals())
