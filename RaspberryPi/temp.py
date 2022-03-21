#from sqlite3 import Cursor
import Adafruit_DHT 
import paho.mqtt.client as mqtt
import json  
import time
from datetime import datetime, timezone, timedelta
from pytz import timezone
import LCD1602

LCD1602.init(0x3f, 1)   # init(slave address, background light)
time.sleep(2)



    
tz = timezone('Asia/Taipei')
now = datetime.now(tz)
humidity, temperature = Adafruit_DHT.read_retry(11,4)



while(1):
    # Show Web Message
    client = mqtt.Client()
    client.username_pw_set("jane","zxc123asd")
    client.connect("192.168.168.77", 1883, 60)
    # Show Humidity And Temperature
    if humidity is not None and temperature is not None:
        try:
            print('Press Ctrl-C To Stop')
            LCD1602.write(0, 0,"Temp: {}                ".format(temperature))
            LCD1602.write(0, 1,"Hum: {}                ".format(humidity))
            time.sleep(1)
        except KeyboardInterrupt:
            print('Close Program')
                
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        payload = {'Temperature' : temperature , 'Humidity' : humidity,'Time':str(now.hour)+":"+str(now.minute)}
        print (json.dumps(payload))
        #要發布的主題和內容
        client.publish("Try/MQTT/Temperature_humidity", json.dumps(payload))
        time.sleep(2)
    else:
            print("Failed to retrieve data from HDT22 sensor")