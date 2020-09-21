import requests
import json
from arcgis.features import FeatureLayer
from arcgis.gis import GIS
from arcgis import features

gis = GIS("https://www.arcgis.com", "devlaahernandezgo", "fQ2HFMfk5ya7E9J")

url = 'https://services5.arcgis.com/otu0qUsUpyUjfoF3/arcgis/rest/services/informacion_lugar/FeatureServer/0'
layer = FeatureLayer(url)


# for x in range (0,9):
# 	body = {"geometry" : {
# 			"objectId": 2,
# 			"x": -74.07,
# 			"y": 4.7-random.random(),
# 			"spatialReference": {
# 				"wkid": 4326
# 			}
# 		},
# 		"attributes" : {
# 			"edificio" : "Aqui porfin",
# 			"nombre" : "prueba",
# 			"numero_interno" : "001",
# 			"maxima_ocupacion" : "18",
# 			"tasa" : random.randrange(0,18),
# 			"tiempo_promedio":"30",
# 			"indice_bioseguro":"70"
# 			}
# 		}
# 	layer.edit_features(adds = [body])


def post_layer_point(capacidad,nombre,cantidad,incice,tiempo_promedio,numero_int,cor_x,cor_y):
    bodyk = {"geometry" : {
			"objectId": 2,
			"x": cor_x,
			"y": cor_y,
			"spatialReference": {
				"wkid": 4326
			}
		},
		"attributes" : {
			"edificio" :"Unal",
			"nombre" : nombre,
			"numero_interno" : numero_int,
			"maxima_ocupacion" : capacidad,
			"tasa" :cantidad ,
			"tiempo_promedio":tiempo_promedio,
			"indice_bioseguro":incice
			}
		}
    layer = FeatureLayer(url)
    layer.edit_features(adds = [bodyk])


