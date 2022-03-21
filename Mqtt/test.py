#from sqlite3 import Cursor
import paho.mqtt.client as mqtt
import json  

client = mqtt.Client()
client.username_pw_set("jane","zxc123asd")
client.connect("192.168.168.77", 1883, 60)

payload = {'Temperature' : 2 , 'Humidity' : 5}
client.publish("Try/MQTT/Test/Temperature_humidity", json.dumps(payload))