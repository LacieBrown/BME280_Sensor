# Author: Lacie Brown 
# Date	: 
# Discp	: This program will read the GPS data that the drone is putting out. It is
#       : kept in the NMEA format which is Latitude = DDMM.MMMMM and Longitude =
#       : Longitude = DDDMM.MMMMM, decimals may vary. Simple conversions can be
#       : done within another function if a different format is desired. 
# File  : home/pi/BME280_Sensor/gps.py

import time
import serial

def init_serial():
    port = "/dev/ttyAMA0"
    global ser
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = port
    ser.timeout = 0.5
    ser.open()

def GPS_Data():
    init_serial()
    data = (str)(ser.readline())
    if data[0:6] == "$GPGGA":
        d = data.split(",")
        if d[7] == "0":
            print("There is no GPS data")
        else:
            latitude = d[2]
            latitude_diriection = d[3]
            longitude = d[4]
            longitude_direction = d[5]
            dict = {"latitude" : latitude, "latitude_direction = " : latitude_direction,
                    "longitude": longitude, "longitude_direction": longitude_direction}
            return dict
        
        
