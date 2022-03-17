#from sqlite3 import Cursor
import Adafruit_DHT 
import paho.mqtt.client as mqtt
import random
import json  
import datetime 
import time

client = mqtt.Client()
client.username_pw_set("jane","zxc123asd")
client.connect("192.168.168.77", 1883, 60)
while True:
    humidity, temperature = Adafruit_DHT.read_retry(11,4)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        payload = {'Temperature' : temperature , 'Humidity' : humidity}
        print (json.dumps(payload))
        #要發布的主題和內容
        client.publish("Try/MQTT/Temperature_humidity", json.dumps(payload))
        time.sleep(2)
    else:
        print("Failed to retrieve data from HDT22 sensor")