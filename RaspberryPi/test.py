import paho.mqtt.client as mqtt
import LCD1602
import time
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Try/MQTT/Test/Temperature_humidity")
def on_message(client, userdata, msg):
    # 轉換編碼utf-8才看得懂中文
    print(msg.topic+" "+ msg.payload.decode('utf-8'))
    payload=json.loads(msg.payload)
    LCD1602.write(0, 0,"Input:               ",True)
    LCD1602.write(0, 1,"{}".format(payload['Input']))

LCD1602.init(0x3f, 1)   # init(slave address, background light)

time.sleep(2)
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("jane","zxc123asd")
client.connect("192.168.168.77", 1883, 60)
client.loop_forever()