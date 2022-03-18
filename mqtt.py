import paho.mqtt.client as mqtt
import psycopg2
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Try/MQTT/Temperature_humidity")
def on_message(client, userdata, msg):
    # 轉換編碼utf-8才看得懂中文
    print(msg.topic+" "+ msg.payload.decode('utf-8'))
    payload=json.loads(msg.payload)
    try:
        connection = psycopg2.connect(user="kxyducmecdyggn",  # 預設使用者
                                      password="3f5caf7284ee638bbe0dba843a9ee2a18a5b6bba033db1c9b3a0b449bdb33e6e",  # 登入密碼
                                      host="ec2-52-70-186-184.compute-1.amazonaws.com",
                                      port="5432",
                                      database="d1j1m9fni09apj")  # 要連結的資料庫
        print("Success Connect")
        cursor = connection.cursor()
        postgreSQL_insert_Query = 'INSERT INTO ht_temperature_humidity(temperature,humidity,create_date) VALUES ({0},{1},\'{2}\')'.format(payload['Temperature'],payload['Humidity'],payload['Time'])
        cursor.execute(postgreSQL_insert_Query)
        connection.commit()
        print("Success Save Data")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
   
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("jane","zxc123asd")
client.connect("192.168.168.77", 1883, 60)
client.loop_forever()