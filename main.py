import re 
import json 


#traer el json
with open('/home/oem/progrmacion-I/parcial/equipo,json','r') as data:
    datos =json.load(data)
    jugadores = datos['jugadores']

def all_jugadores():
    for indice in jugadores:
        print('{0}: {1}'.format(indice['nombre'],indice['posicion']))


all_jugadores();