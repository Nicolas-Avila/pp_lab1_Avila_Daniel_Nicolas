import re 
import json

with open('/home/oem/progrmacion-I/parcial/equipo,json','r') as data:
    datos =json.load(data)
    jugadores = datos['jugadores']

def mostrar(imprimir)->None:
    '''
    la funcion muestra en consola lo que se le pase.
    '''
    print(imprimir)

def lista_vacia()->None:
    '''
    Averigua si la lista esta vacia.
    '''
    if len(jugadores) == 0:
        mostrar("Lista esta vacía no puedo realizar ninguna operacion.")
        exit()#para terminar la ejecucion del programa
    else:
        mostrar('BIENVENIDO!!')

#1
def all_jugadores()->None:
    '''
    la funcion recoree todo el json y muestra los nombres y la posicion de los jugadores.
    '''
    for indice in jugadores:
        mostrar('{0}: {1}'.format(indice['nombre'],indice['posicion']))

#2
def un_jugador(ingreso:int)-> None:    
    '''
    Recive un entero. 
    La funcion muestra nombre posicion y estadisticas de la posicion ingresada.
    guarda el archivo en un csv.
    '''
    estadistica=[]
    datos = []
    if (ingreso <= len(jugadores)):
        mostrar('{0}\n{1}\n'.format(jugadores[ingreso]['nombre'],jugadores[ingreso]['posicion']))
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
    Recive un entero.
    Funciona como un buscador y muestra los logros de los jugadores buscados. 
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
    Recive un string.
    Averigua si el jugador pertenece al salon de la fama.
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
    Recive un string.
    Averigua cual es valor maximo de la key ingresada.
    Retorna un mensaje.
    '''
    maximo=0
    for indice in jugadores:
        for i , valor in indice['estadisticas'].items():
            if i == key:
                if maximo < valor:
                    jugador = indice['nombre']
                    maximo = valor
    key = key.replace('_',' ')
    return mostrar('la mayor cantidad de {0} la tiene el jugador {2} con {1} {0}'.format(key,maximo,jugador))

#9,10,11,14,17
def jugador_rendimiento(key:str,ingreso:int)->None:
    '''
    Recibe un string y un entero. 
    Averigua los jugadores con el valor mayor que se ingreso. 
    '''
    jugador = []
    
    for indice in jugadores:
        for i , valor in indice['estadisticas'].items():
            if i == key:
                if ingreso < valor:
                    jugador.append(indice['nombre'])
        if len(jugador) == 0:
            jugador.append('ninguno')
    key = key.replace('_',' ')
    mostrar('los jugadores que tiene mas {0} del valor ingresado ({1}) son:'.format(key,ingreso))
    for nombre in jugador:
        print(nombre, end=' ')

#15
def puntos_totales()->None:
    '''
    Calcula el promedio de los puntos por partidos sacando al jugador con menos puntos.
    '''
    minimo = 0
    acumulador = 0
    cont = -1
    for indice in jugadores:
        for i,valor in indice['estadisticas'].items():
            if i == 'promedio_puntos_por_partido':
                acumulador= acumulador + valor
                cont += 1
                if minimo == 0 or minimo > valor:
                    minimo = valor
    acumulador_total = acumulador - minimo
    porcentaje = acumulador_total / cont
    porcentaje= round(porcentaje,2)
    mostrar('la cantidad de puntos por partido sacando al peor jugador es de {0}'.format(porcentaje))

#16
def mayor_logros()->None:
    '''
    Averigua que jugador tiene mas logros. 
    '''
    mas_logros = 0
    for indice in jugadores:
        logros=len(indice['logros'])
        if mas_logros < logros:
            jugador = indice['nombre']
            mas_logros = logros
    
    mostrar('el jugador con mas logros es {0} con {1} logros'.format(jugador, mas_logros))

#4 es el unto 5
def alfabetico()->None:
    '''
    Muestra el porcentaje de puntos por partido y ordena los jugadores de forma alfabeticamente.
    '''
    acumulador = 0
    cont = 0
    lista_nombre = []
    for jugador in jugadores:
        lista_nombre.append(jugador['nombre'])
        for dato, puntos in jugador['estadisticas'].items():
            if dato == 'promedio_puntos_por_partido':
                acumulador = acumulador + puntos
                cont =+ 1
    porcentaje = acumulador / cont
    porcentaje = round(porcentaje, 2)
    mostrar('el porcentaje de puntos por partido es de {0}\ny el orden alfabetico es:'.format(porcentaje))
    ordenar_lista(lista_nombre)
    for nombre in lista_nombre:
        mostrar(nombre)

#19 es el punto 20
def orden_pisicion(key,ingreso)->None:
    '''
    Averigua el mayor del numero ingresado y ordenas los nombres alfabeticamente.
    '''
    jugador = []

    for indice in jugadores:
        for i , valor in indice['estadisticas'].items():
            if i == key:
                if ingreso < valor:
                    jugador.append(indice['nombre'])
    key = key.replace('_',' ')
    mostrar('los jugadores que tiene mas {0} del valor ingresado ({1}) son:'.format(key,ingreso))
    ordenar_lista(jugador)
    
    for nombre in jugador:
        print(nombre, end='\n')


def ordenar_lista(lista:list)->list:
    '''
    Recibe por paramtro una lista.
    La ordena alfabeticamente / numericamente de forma ascendente.
    Retorna la lista ordenada. 
    '''
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

#extra 1
def cantidad_posicion()->None:
    '''
    Recorre la las posiciones y cuenta la cantidad de posisiones iguales y lo guarda en un diccionario.
    '''
    dic = {}
    for jugador in jugadores:
        if jugador['posicion'] in dic:
            dic[jugador['posicion']] += 1
        else:
            dic[jugador['posicion']] = 1
    for posicion , valor in dic.items():
        mostrar('posicion {0} cantidad {1}'.format(posicion,valor))

#extra 2
def all_star()->None:
    '''
    Ordena y mustra la cantidad de veces que consiguieron el All-Star.
    '''
    orden = []
    for jugador in jugadores:
        all_star = {}
        all_star['nombre'] = jugador['nombre']

        for logro in jugador['logros']:
            if re.search('All-Star$',logro):
                veces=logro.split()
                veces = int(veces[0])
                all_star['veces'] =  veces
                orden.append(all_star)
                #?toma como entrada un elemento de la lista y devuelve el valor asociado a la clave 'veces' de ese diccionario
                #?lambda crea una funcion anonima
                ordenado = sorted(orden, key=lambda x: x['veces'], reverse=True)
    for star in ordenado:
        print('{0} {1} veces all star'.format(star['nombre'],star['veces']))

#extra 3
def mejores_estadisticas()->None:
    '''
    Averigua quien tiene las mejores estadisticas usando la funcion estadistica_mayor.
    '''
    for indice in jugadores:
        for dato, puntos in indice['estadisticas'].items():
            estadistica_mayor(dato)
        break

#extra 4
def el_mejor()->None:
    '''
    Averigua que jugador tiene las mejores estadisticas.
    '''
    jugador_max=None
    max_puntaje=0
    
    for jugador in jugadores:
        estadistica_total=0
        for estadistica in jugador["estadisticas"].values():
            estadistica_total+=estadistica

        if jugador_max is None or estadistica_total < max_puntaje:
            jugador_max=jugador
    print("el jugador que tiene mejores estadisticas es: {0}".format(jugador_max["nombre"]))

