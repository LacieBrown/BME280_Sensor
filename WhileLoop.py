# Author:
# Date	:
# Discp	: This program will run the BME280_Sensor in a while loop. Then it
# 	: will send this data to a website to display the sensor readings 
# 	: along with the drone's data. 
#

import BME280_Sensor as bme280
import time


while(True): 
	bme280.DisplayData()
	time.sleep(5)
	clear() 



