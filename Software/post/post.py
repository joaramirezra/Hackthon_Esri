import requests
import json
from arcgis.features import FeatureLayer
from arcgis.gis import GIS
from arcgis import features
import random
gis = GIS("https://www.arcgis.com", "devlaahernandezgo", "fQ2HFMfk5ya7E9J")

url = 'https://services5.arcgis.com/otu0qUsUpyUjfoF3/arcgis/rest/services/informacion_lugar/FeatureServer/0'
layer = FeatureLayer(url)

for x in range (0,9):
	body = {"geometry" : {
			"objectId": 2,
			"x": -74.07,
			"y": 4.7-random.random(),
			"spatialReference": {
				"wkid": 4326
			}
		},
		"attributes" : {
			"edificio" : "Aqui porfin",
			"nombre" : "prueba",
			"numero_interno" : "001",
			"maxima_ocupacion" : "18",
			"tasa" : random.randrange(0,18),
			"tiempo_promedio":"30",
			"indice_bioseguro":"70"
			}
		}
	layer.edit_features(adds = [body])

print(layer.query().sdf)

