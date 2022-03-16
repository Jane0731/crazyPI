import Adafruit_DHT 

#DHT_SENSOR = Adafruit_DHT.DHT22 
#DHT_PIN = 4  

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11,4)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Failed to retrieve data from HDT22 sensor")