# Author:
# Date	:
# Discp	: This program will run the BME280_Sensor in a while loop. Then it
# 	: will send this data to a website to display the sensor readings 
# 	: along with the drone's data. 
#

import BME280_Sensor as bme280
import time
import os

user_input = raw_input('Press any key to start or "x" to quit') 

bme280.DisplayChipData()
while(True):
    bme280.DisplayData()
    print("\n")
    print("\n")


