import serial
import time

ser = serial.Serial('/dev/ttyUSB1',115220)

def  leer_macs_tiempo(tiempo_segundos):
	timeout = time.time() +  tiempo_segundos
	mac_list = {}
	while True:
		if(time.time() > timeout):
			break
		else :
			input_mac = ser.readline()
			mac_list[input_mac] = input_mac 
	
	return mac_list	

def  imprimir_macs(tiempo_segundos):
	timeout = time.time() +  tiempo_segundos
	mac_list = {}
	while True:
		if(time.time() > timeout):
			break
		else :
			input_mac = ser.readline()
			print(input_mac) 
	
	return mac_list	