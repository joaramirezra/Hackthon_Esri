from port import *
from post_layer import *
import random
import requests
import json
from arcgis.features import FeatureLayer
from arcgis.gis import GIS
import time
from arcgis import features


gis = GIS("https://www.arcgis.com", "devlaahernandezgo", "fQ2HFMfk5ya7E9J")
url = 'https://services5.arcgis.com/otu0qUsUpyUjfoF3/arcgis/rest/services/informacion_lugar/FeatureServer/0'
layer = FeatureLayer(url)

Factor = 3 # numero de dispositivos por persona y routers 
old_mac_list = {}

Cantidad_auditorios = [20,25,20,20,25,27,28,29]
tamaño_auditorio_metros2 = [80,80,50,50,70,70,80,80]
indice_ventilacion_auditorio = [5,5,5,5,3,3,2,1]
cordenadas = [[-74.081392,4.638479],[-74.084473,4.637417 ],[-74.082354,4.639011],
			[-74.084741,4.637973 ],[-74.083881,4.634435],[-74.082723, 4.634408],
			[-74.080663,4.636226],[-74.087229,4.638846]]

nombre_auditorios =["auditorio Virgilio Tejada","auditorio Marie Curie",
		"auditorio Johan Ramirez","auditorio Pedro Cardenaz",
		"auditorio Juan perez","auditorio Camilo Torres",
		"auditorio Leon De Greiff","auditorio Dolly perez"]

# for k in mac_list:
# 	print(k)

indice_k = [] 
for salon in range(8):
	indice_k.append(tamaño_auditorio_metros2[salon]*indice_ventilacion_auditorio[salon])


def ejecutar(tiempo_segundos):
	timeout = time.time() +  tiempo_segundos	
	while True:
		if(time.time() > timeout):
			for valor in range(0,8):
				layer_features = layer.query().features[0].attributes['OBJECTID']
				layer.edit_features(deletes =str(layer_features))
			for salon in range(8):
				mac_list = {}
				mac_list = leer_macs_tiempo(1)
				Cantidad_personas = round(len(mac_list)/Factor)
				indice_bioseguro = indice_k[salon]/(Cantidad_auditorios[salon]-Cantidad_personas)
				tiempo_permanencia = random.randrange(15,90)
				numero = salon
				nombre = nombre_auditorios[salon]
				capacidad = Cantidad_auditorios[salon]
				post_layer_point(capacidad,nombre,Cantidad_personas,int(indice_bioseguro),tiempo_permanencia,
								numero,cordenadas[salon][0],cordenadas[salon][1])
			break
		else :
			imprimir_macs(3)
			pass

while True :
	ejecutar(30)
	#print(layer.query().sdf)
	time.sleep(30)