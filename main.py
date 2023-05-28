import re 
from funciones import (
    lista_vacia,
    all_jugadores,
    un_jugador,
    logros,
    promedio_puntos,
    salon_fama,
    estadistica_mayor,
    jugador_rendimiento,
    puntos_totales,
    mayor_logros,
    

    )
lista_vacia()
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
        nombre = input('ingrese un jugador a buscar: ').capitalize()
        logros(nombre)

    case 4:
        #no terminado 
        promedio_puntos()

    case 5:
        nombre = input('ingrese un jugador a buscar: ')
        salon_fama(nombre.capitalize())

    case 6:
        estadistica_mayor('rebotes_totales')

    case 7:
        estadistica_mayor('porcentaje_tiros_de_campo')

    case 8:
        estadistica_mayor('asistencias_totales')

    case 9:
        valor = input('ingrese un valor: ')
        if re.match('[0-9]',valor):
            jugador_rendimiento('promedio_puntos_por_partido',int(valor))

    case 10:
        valor = input('ingrese un valor: ')
        if re.match('[0-9]',valor):
            jugador_rendimiento('promedio_rebotes_por_partido',int(valor))
        
    case 11:
        valor = input('ingrese un valor: ')
        if re.match('[0-9]',valor):
            jugador_rendimiento('promedio_asistencias_por_partido',int(valor))
    
    case 12:
        estadistica_mayor('robos_totales')

    case 13:
        estadistica_mayor('bloqueos_totale')

    case 14:
        valor = input('ingrese un valor: ')
        if re.match('[0-9]',valor):
            jugador_rendimiento('porcentaje_tiros_libres',int(valor))
        else:
            print('no es un numero')

    case 15:
        puntos_totales()

    case 16:
        mayor_logros()

    case 17:
        valor = input('ingrese un valor: ')
        if re.match('[0-9]',valor):
            jugador_rendimiento('porcentaje_tiros_triples',int(valor))
        else:
            print('no es un numero')

    case 18:
        estadistica_mayor('temporadas')

    case 19:
        pass

    case _:
        print('Oh no °-° \nesa opcion no existe')
