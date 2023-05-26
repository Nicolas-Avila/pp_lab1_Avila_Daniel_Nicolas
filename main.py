import re 
import json 
from funciones import (
    all_jugadores,
    un_jugador,
    logros,
    promedio_puntos,
    salon_fama,
    estadistica_mayor,
    jugador_rendimiento

    )

#menu

menu = int(input('ingrese una opcion: '))
#re.match('[0-9]',menu)
match (menu):
    case 1:
        all_jugadores()
        

    case 2:
        ingreso = int(input('ingrese el numero del jugador: '))
        un_jugador(ingreso)

    case 3:
        pass

    case 4:
        nombre = input('ingrese un jugador a buscar: ').capitalize()
        logros(nombre)

    case 5:
        promedio_puntos()

    case 6:
        nombre = input('ingrese un jugador a buscar: ')
        salon_fama(nombre.capitalize())

    case 7:
        estadistica_mayor('rebotes_totales')

    case 8:
        estadistica_mayor('porcentaje_tiros_de_campo')

    case 9:
        estadistica_mayor('asistencias_totales')

    case 10:
        valor = int(input('ingrese un valor: '))
        jugador_rendimiento('promedio_puntos_por_partido',valor)
    case _:
        print('tonto')
