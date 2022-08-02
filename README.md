# CRAZYPI
## 執行流程
![FlowChart](/flowchart.png)
## 成果展示
### CRAZYPI 畫面
![CrazyPi](/CrazyPi.gif)
### RaspberryPi 漂亮的雜誌封面圖
![RaspberryPi](/RaspberryPi.jpg)

## Web Folder
使用django架站~  

### 負責功能?
- 提供 API 給 jQuery.ajax 定時爬取資料庫資料
- html 使用 jQuery.ajax、setInterval、Chart.js 每秒將資料庫資訊(溫度、濕度、時間)呈現給使用者

### 如何執行?
1. 本地端安裝Django，可參考此篇文章[架設 Django 開發環境](https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/development_environment)
2. 安裝 環境pip

        pip install -r requirements.txt
3. 執行
       
        python manage.py runserver
## Mqtt Folder
### 負責功能?
- 與MQTT Server做連線
- 與PostgreSQL連線
- 訂閱主題，並且將溫溼度感測器的數據存進資料庫   
### 如何執行?
1. 本地端安裝mosquitto，可參考此篇文章[認識 MQTT 與安裝 Mosquitto Windows 版本](https://jimirobot.tw/esp32-mosquitto-windows-mqtt-tutorial/)
2. 啟動MQTT Server，可參考此篇文章[Mosquitto conf 設定與 MQTT 測試](https://jimirobot.tw/esp32-mosquitto-conf-mqtt-tutorial/)
3. 切換路徑至Mqtt Folder，隨後執行mqtt.py檔
```bash=
cd Mqtt
Python mqtt.py
```
## RaspberryPi Folder
### 負責功能?
- 與MQTT Server做連線
- 接收溫溼度感測器的數據
- 新增主題，並且將溫溼度感測器的數據包成內容，發布出去   
### 如何執行?
切換路徑至RaspberryPi Folder，隨後執行temp.py檔
```bash=
cd RaspberryPi
Python temp.py
```
