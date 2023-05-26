import re 
import json

with open('/home/oem/progrmacion-I/parcial/equipo,json','r') as data:
    datos =json.load(data)
    jugadores = datos['jugadores']

def mostrar(imprimir):
    print(imprimir)

#1
def all_jugadores()->None:
    '''
    la funcion recoree todo el json y muestra los nombres y la posicion de los jugadores
    '''
    for indice in jugadores:
        mostrar('{0}: {1}'.format(indice['nombre'],indice['posicion']))

#2
def un_jugador(ingreso:int)-> None:    
    '''
    Recive un entero 
    La funcion muestra nombre posicion y estadisticas de la posicion ingresada
    '''
    if (ingreso <= len(jugadores)):
        mostrar('{0}\n{1}\n'.format(jugadores[ingreso]['nombre'],jugadores[ingreso]['posicion']))
        for indice, valor in jugadores[ingreso]['estadisticas'].items():
            mostrar('{0}: {1}'.format(indice, valor))

#4 arreglar bug
def logros(nombre:int)->None:
    '''
    recive un entero
    la funcion funciona como un buscador y muestra los logros de los jugadores buscados 
    '''
    encontrado = False
    for jugador in jugadores:
        if (re.search(nombre,jugador['nombre'])):
            mostrar('\n{0}\nSus logros:'.format(jugador['nombre']))
            for logro in jugador['logros']:
                mostrar('{0}'.format(logro))
                encontrado = True
        elif encontrado == False: 
            mostrar('Ese jugador no se pudo encontrar intente de nuevo')
            nombre = input('ingrese un jugador a buscar: ')
            logros(nombre)

#5 falta la cuenta y el ordenamiento
def promedio_puntos():
    acumulador = 0
    
    for indice in jugadores:
        acumulador = acumulador + indice['estadisticas']['promedio_puntos_por_partido']
        acumulador = round(acumulador,2)#limita a 2 numeros con coma y redondea
        print(acumulador)

#6 bug del 4
def salon_fama(nombre):
    encontrado = False
    ave = 'Miembro del Salon de la Fama del Baloncesto'
    for jugador in jugadores:
        if (re.match(nombre,jugador['nombre'])):
                print('encontre')
                if ave in jugador['logros']:
                    encontrado=True
                    mostrar('si pertenece al salon de la fama')
                elif encontrado==False:
                    mostrar('no pertenece al salon de la fama')

#7#8#9
def estadistica_mayor(key:str)->None:
    '''
    recive un string
    averigua cual es valor maximo de la key
    '''
    maximo=0
    for indice in jugadores:
        for i , valor in indice['estadisticas'].items():
            if i == key:
                if maximo < valor:
                    jugador = indice['nombre']
                    maximo = valor
    key = key.replace('_',' ')
    mostrar('la mayor cantidad de {0} la tiene el jugador {2} con {1} {0}'.format(key,maximo,jugador))

#10
def jugador_rendimiento(key:str,ingreso:int):
    jugador = []
    for indice in jugadores:
        for i , valor in indice['estadisticas'].items():
            if i == key:
                if ingreso < valor:
                    jugador.append(indice['nombre'])
    key = key.replace('_',' ')
    mostrar('los jugadores que tiene mas {0} del valor ingresado ({1}) son:'.format(key,ingreso))
    for nombre in jugador:
        print(nombre, end=' ')

