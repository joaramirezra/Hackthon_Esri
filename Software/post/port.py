import serial
import time
import csv

ser = serial.Serial('/dev/ttyUSB1',115220)

while True:
	try:
		print(ser.readline())
	except:
		pass
