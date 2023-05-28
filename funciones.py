import re 
import json

with open('/home/oem/progrmacion-I/parcial/equipo,json','r') as data:
    datos =json.load(data)
    jugadores = datos['jugadores']

def mostrar(imprimir)->None:
    '''
    la funcion muestra en consola lo que se le pase
    '''
    print(imprimir)

def lista_vacia():
    '''
    averigua si la lista esta vacia
    '''
    if len(jugadores) == 0:
        mostrar("Lista esta vacía no puedo realizar ninguna operacion.")
        exit()#para terminar la ejecucion del programa
    else:
        mostrar('BIENVENIDO!!')



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
    guarda el archivo en un csv
    '''
    estadistica=[]
    datos = []
    if (ingreso <= len(jugadores)):
        mostrar('{0}\n{1}\n'.format(jugadores[ingreso]['nombre'],jugadores[ingreso]['posicion']))
        datos.append(jugadores[ingreso]['nombre'])
        estadistica.append(jugadores[ingreso]['posicion'])
        for indice, valor in jugadores[ingreso]['estadisticas'].items():
            mostrar('{0}: {1}'.format(indice, valor))
            estadistica.append(indice)
            datos.append(str(valor))

        dato_str = ','.join(datos)
        estadistica_str = ','.join(estadistica)
        datos_csv =  estadistica_str + '\n'+ dato_str
        with open ('/home/oem/progrmacion-I/parcial/csv.csv','w')as archivo:
            archivo.writelines(datos_csv)
            mostrar('el archivo se guardo')
    else:
        mostrar('ese jugador no existe')

#3 
def logros(nombre:int)->None:
    '''
    recive un entero
    la funcion funciona como un buscador y muestra los logros de los jugadores buscados 
    '''
    encontrado = False 
    for jugador in jugadores:
        if (re.search(nombre,jugador['nombre'])):
            mostrar('{0}\nSus logros:'.format(jugador['nombre']))
            for logro in jugador['logros']:
                mostrar('{0}'.format(logro))
                encontrado = True
    if encontrado == False: 
        mostrar('Ese jugador no se pudo encontrar intente de nuevo')
        nombre = input('ingrese un jugador a buscar: ').capitalize()
        logros(nombre)

#5
def salon_fama(nombre:str)->None:
    '''
    recive un string
    averigua si el jugador pertenece al salon de la fama
    '''
    encontrado = False
    salon = 'Miembro del Salon de la Fama del Baloncesto'
    for jugador in jugadores:
        if (re.match(nombre,jugador['nombre'])):
                if salon in jugador['logros']:
                    encontrado=True
                    mostrar('{0} si pertenece al salon de la fama'.format(jugador['nombre']))
                elif encontrado==False:
                    mostrar('{0} no pertenece al salon de la fama'.format(jugador['nombre']))

#6,7,8,12,13,18
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

#9,10,11,14,17
def jugador_rendimiento(key:str,ingreso:int)->None:
    '''
    recibe un string y un int 
    averigua los jugadores con mayor valor ingresado 
    '''
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

#15
def puntos_totales()->None:
    '''
    calcula el promedio de los puntos por partidos sacando al peor jugador
    '''
    minimo = 0
    acumulador = 0
    cont = 0
    for indice in jugadores:
        for i,valor in indice['estadisticas'].items():
            if i == 'promedio_puntos_por_partido':
                acumulador= acumulador + valor
                cont += 1
                if minimo == 0 or minimo > valor:
                    
                    minimo = valor
    acumulador_total = acumulador - minimo
    cont -=1
    porcentaje = acumulador_total / cont
    porcentaje= round(porcentaje,2)
    print(cont)
    mostrar('la cantidad de puntos por partido sacando al peor jugador es de {0}'.format(porcentaje))

#16
def mayor_logros()->None:
    '''
    averigua que jugador tiene mas logros 
    '''
    mas_logros = 0
    for indice in jugadores:
        logros=len(indice['logros'])
        if mas_logros < logros:
            jugador = indice['nombre']
            mas_logros = logros
    
    mostrar('el jugador con mas logros es {0} con {1} logros'.format(jugador, mas_logros))

