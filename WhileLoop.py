# Author:
# Date	:
# Discp	: This program will run the BME280_Sensor in a while loop. Then it
# 	: will send this data to a website to display the sensor readings 
# 	: along with the drone's data. The program also does a write to
#       : file function, the file directory is below. 
# File  : home/pi/BMESensorProject 


import BME280_Sensor as bme280
import time
import os
import sys
import datetime
import json
    
false = KeyboardInterrupt
file_name = open("SensorData.txt", "a+") 
# Display File name data so the user can find the stored data on the local Pi
print("The file name is ", file_name.name)
print("The file is either closed or not ", file_name.closed)
print("The opening mode of the file is ", file_name.mode)

# Chip Data is displayed first and only once. 
print('Chip Data')
bme280.DisplayChipData()

# Display the date and time for clean data collection
time = time.time()
dattime = datetime.datetime.fromtimestamp(time).strftime('Today is: ''%Y-%m-%d \nThe time is: ''%H:%M:%S')
print(dattime)

#Get users input to begin displaying sensor readings
user_input = raw_input("\nPress enter to begin and CTRL C to quit \n")

# Output Sensor reading to screen in a loop until CTRL C is pressed
try:
    while(True):
        bme280.DisplayData()
        # save data, possible solution 
        with open("SensorData", "a+") as f:
            json.dump(bme280.DisplayData(), f)
        print("\n")
# When CNTR C is pressed, finish by saving to a file 
except false:
    print("\nInterrupted,  closing out")
    f.close()

# Exit the program
sys.exit()

