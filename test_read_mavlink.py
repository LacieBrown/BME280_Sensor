import time
import os
from time import sleep 
import sys
import drone_mav
import dronekit

port = '/dev/ttyAMA0'

try:
    print "I entered the try"
    vehicle = dronekit.connect(port, wait_ready=None, baud=57600)
    print("I have now connected to the vehicle: ", vehicle)
    print " GPS: %s" % vehicle.gps_0
    
    while(True):
        print "I entered the while"   
# Get the GPS data from the MAVLink on the drone
        print " GPS: %s" % vehicle.gps_0
        lat = vehicle.location.global_frame.lat
        print "I just read lattitude"
        lon = vehicle.location.global_frame.lon
        print "I read Longitude"
        alt = vehicle.location.global_frame.alt
        print "I read altitude"
# Print the data 
        print("Lat = ", lat)
        print "lat is displayed"

        print("Lon = ", lon)
        print "lon is display"
        print("Alt = ", alt)
        print "alt was just displayed"
        sleep(1)
        
except KeyboardInterrupt:
    print "CTRL^C Pressed, exiting"
    sys.exit()
