from flask import Flask, render_template
#import RPi.GPIO as GPIO
#import Adafruit_DHT as dht
import json, time
#import dht11
#from pyngrok import ngrok
from flask_cors import CORS, cross_origin
import mysql.connector
import random
 
app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/')
def home_page():
    db = mysql.connector.connect(
        user = 'root',
        password = 'rinriN@DBM01',
        host = '118.21.158.208',
        database = 'sensor',
        auth_plugin='mysql_native_password',
        raise_on_warnings=True,
    )

    cursor = db.cursor(buffered=True)	
    
    try:
        #cursor = self.db.cursor()
        cursor.execute("SELECT TEMPERATURE, HUMIDITY FROM dht11 ORDER BY DATE DESC, TIME DESC LIMIT 1")
        data = cursor.fetchone()

        temp = int(data[0])
        humi = int(data[1])
        
        db.commit()

        data_set = {'API Name':'sensorapi', 'Status':'Successfully loaded...', 'Timestamp':time.asctime(time.localtime(time.time())), 'Temperature':temp, 'Humidity':humi}
        json_dump = json.dumps(data_set)

        cursor.close()
        db.close()

        return json_dump
    except Exception as error:
        data_set = {'API Name':'sensorapi', 'Status':'Unsuccessfully loaded, Please try again later...'}
        json_dump = json.dumps(data_set)
        cursor.close()
        db.close()
        return json_dump

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=False)
