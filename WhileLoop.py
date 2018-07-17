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
import csv
    
false = KeyboardInterrupt
f = open("SensorData.txt", "a+") 
# Display File name data so the user can find the stored data on the local Pi
print("The file name is ", f.name)
print("The file is either closed or not ", f.closed)
print("The opening mode of the file is ", f.mode)

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
        bme280.SensorDataDict1()
        bme280.SensorDataDict2()
        print("\n")

        # Save Info to text file (Option 1)
        f = open("SensorData.txt", "a+")
        f.wrtie(str(dict))
        f.close
        # Save info to csv file (Option 2) (Excel)
        w = csv.writer(open("SensorData.csv", "w"))
        for key, val in dict.items():
            w.writerow([key, val])
        
# When CNTR C is pressed, finish by saving to a file 
except false:
    print("\nInterrupted,  closing out")
    f.close() # final check to see if the txt file is closed 

# Exit the program
sys.exit()


