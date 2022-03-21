from django.shortcuts import render
import paho.mqtt.client as mqtt 
import json   
import time 

def home(request):
    # 連接到linux
    client = mqtt.Client()
    client.username_pw_set("jane","zxc123asd")
    client.connect("192.168.168.77", 1883, 60)

    if request.method == 'POST': 
        #要發布的主題和內容
        text = request.POST['display']
        if len(text) < 16:
            text = text+"                "
        payload = {'Input' : text }
        client.publish("Try/MQTT/Test/Temperature_humidity", json.dumps(payload))
        time.sleep(2)
    else:
        print("Failed to retrieve data from HDT22 sensor")

    return render(request,'crazypi.html', locals())
