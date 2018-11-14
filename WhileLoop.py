# Author: Lacie Brown 
# Date	:
# Discp	: This program will run the BME280_Sensor data in a while loop. Then it
# 	: will send this data to a website to display the sensor readings 
# 	: along with the drone's gps data. Influxdb is used alongside with grafana
#       : The program also does a write to a text file function. 
# File  : home/pi/BMESensorProject
# File  : SensorData.txt (Text file with run data, saved to local drive) 


import BME280_Sensor as bme280
import time
from time import sleep
import os
import sys
import datetime
import csv
import gps
from influxdb import InfluxDBClientError, InfluxDBClient

false = KeyboardInterrupt

# Setup for connecting to the Influxdb database
user = 'root'
password = 'root'
host = 'localhost'
port = 8086
dbname = "raspi-drone"
sample_time = 1
session = "raspi-drone-session"

# This earses previous data within the txt file, remove "w" if previous run data
# is needed and replace with "a+" 
f = open("SensorData.txt", "w").close()

# Chip Data is displayed first and only once. 
print('Chip Data')
bme280.DisplayChipData()
print('\n')

# Display the date and time for clean data collection and save to txt file as well
time = time.time()
dattime = datetime.datetime.fromtimestamp(time).strftime('Today is: ''%Y-%m-%d \nThe time is: ''%H:%M:%S')
f = open("SensorData.txt", "a+")
f.write(str(dattime)+"\n")
print(dattime)

#Get users input to begin displaying sensor readings
user_input = input("\nPress enter to begin and CTRL C to quit \n")

# Output Sensor and GPS readings to screen in a loop until CTRL C is pressed
try:
    while(True):
# Take Sensor Readings and Display
        data = bme280.SensorDataDict()
        temperatureC = data["TempC"]
        temperatureF = data["TempF"]
        pressure = data["Pressure"]
        humidity = data["Humidity"]
        print("Temperature = ", temperatureC, "C")
        print("Temperature = ", temperatureF, "F")
        print("Pressure = ", pressure, "hPa")
        print("Humidity = ", humidity, "%")
        print("\n")
        sleep(1)
        
# Take GPS Readings and Display, note only the gps parameters are being read
        gps_data = gps.read_vehicle_gps_parameters()
        latitude = gps_data["latitude"]
        longitude = gps_data["longitude"]
        altitude = gps_data["altitude"]
        print("Latitude = ", latitude)
        print("Longitude = ", longitude)
        print("Altitude = ", altitude)
        print("\n")
        sleep(1)
        
# Save sensor and gps data to text file
        f = open("SensorData.txt", "a+")
        f.write(str(data)+"\n") 
        f.write(str(gps_data)+"\n") 

# Write information to grafana
        grafana_data = [
            {
                "measurement": session,
                "time": time,
                "fields" : { "Temperature_C" : temperatureC,
                             "Temperature_F" : temperatureF,
                             "Pressure"      : pressure,
                             "Humidity"      : humidity,
                             "Latitude"      : latitude,
                             "Longitude"     : longitude,
                             "Altitude"      : altitude
                            }
                }            
        
# When CNTR C is pressed, finish by saving to file
except false:
    print("\nInterrupted,  closing out")
# Write the final readings displayed to the txt file, sleep to make sure info is writen 
    f.write(str(data)+"\n")
    f.write(str(gps_data)+"\n")
    sleep(1) 
# final check to see if the txt file is closed                 
    f.close() 
# Exit the program safely 
sys.exit()


