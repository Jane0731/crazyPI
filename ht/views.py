from django.shortcuts import render
from .models import temperature_humidity
import datetime

def home(request):
    last_one = temperature_humidity.objects.last()
    last= temperature_humidity.objects.all().order_by('-id')[:6]
    print(last[1].humidity)
    last_six = last[5]
    last_five = last[4]
    last_four = last[3]
    last_three = last[2]
    last_two =last[1]
    return render(request,'page.html', locals())
