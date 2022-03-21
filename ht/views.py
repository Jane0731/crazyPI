'''
Author: your name
Date: 2022-03-17 17:47:58
LastEditTime: 2022-03-21 11:48:27
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \crazyPI\ht\views.py
'''
from django.shortcuts import render
from .models import temperature_humidity
import datetime

def home(request):
    print(request.POST.get("display",""))
    print("AAA")
    return render(request,'crazypi.html', locals())
