# Author: Lacie Brown 
# Date	: 
# Discp	: This program will read the GPS data that the drone is putting out through
#       : MAVLink. Dronekit is used to connect to the port the drone is on. It is
#       : also used to read the GPS parameters. 
#       : 
# File  : home/pi/BME280_Sensor/gps.py

import dronekit

port = '/dev/ttyAMA0'

def connect_vehicle():
# Connect to the port using dronekit.connect, baud is set to 57600    
    v = dronekit.connect(port, wait_ready=None, baud=57600)
    return vehicle

def read_vehicle_gps_parameters():
# This function will read the lattitude, longitude, and altitude of the drone. These parameters are
# then put into a dictionary for use in the WhileLoop
    vehicle = connect_vehicle()
    lat = vehicle.location.global_frame.lat
    lon = vehicle.location.global_frame.lon
    alt = vehicle.location.global_frame.alt
    dict = {"latitude" : lat, "longitude" : lon, "altitude" : alt}
    return dict

def read_vehicle_gps():
# This function will read the gps, and output the full gps parameter (I do not know in what format) 
    vehicle = connect_vehicle()
    GPS = vehicle.gps_0
    return GPS
