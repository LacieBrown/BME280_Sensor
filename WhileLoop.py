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

# Chip Data is displayed first and only once. 
print('Chip Data')
bme280.DisplayChipData()
time.sleep(3)

# Display the date and time for clean data collection

time.sleep(2)

#Get users input to begin displaying sensor readings
user_input = input("\nPress enter to begin and CTRL C to quit \n")

# Output Sensor reading to screen in a loop until CTRL C is pressed
try:
    bme280.DisplayData()
    print("\n")
    print("\n")
# When CNTR C is pressed, finish by saving to a file 
finally:
    path = '/home/pi/BMESensorProject/SensorData.txt'
    # Exit the program
    sys.exit()

