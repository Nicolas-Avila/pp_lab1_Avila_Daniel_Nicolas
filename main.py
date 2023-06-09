import re 
from funciones import (
    lista_vacia,
    all_jugadores,
    un_jugador,
    logros,
    salon_fama,
    estadistica_mayor,
    jugador_rendimiento,
    puntos_totales,
    mayor_logros,
    alfabetico,
    orden_pisicion,
    cantidad_posicion,
    all_star,
    mejores_estadisticas,
    el_mejor
    
    

    )
lista_vacia()
#menu


print('menu \n'
      '1.ver a todo los jugadores\n'
      '2.ver a un solo jugador y guardarlo en un cvs\n'
      '3.buscar un jugador por el nombre\n'
      '4.promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente.\n'
      '5.pertenece al salon de la fama?\n'
      '6.el que mas rebotes tiene\n'
      '7.el que mas tiros de campo tiene\n'
      '8.el que mas asistencias tiene\n'
      '9.el que mas puntos tiene segun lo que ingrese\n'
      '10.el que mas rebotes tiene segun lo que ingrese\n'
      '11.el que mas asistencias tiene segun lo que ingrese\n'
      '12.el que mas robos tiene👮‍♀️\n'
      '13.el que mas bloqueos tiene\n'
      '14.el que mas tiros libres tiene segun lo que ingrese\n'
      '15.promedio de puntos por partido del equipo sacando al peor jugador\n'
      '16.el que mas logros tiene\n'
      '17.el que mas tiros triples tiene segun lo que ingrese\n'
      '18.el que mas temporadas jugo\n'
      '19.Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas.')
     

menu = int(input('ingrese una opcion: '))

match (menu):
    case 1:
        all_jugadores()
        

    case 2:
        ingreso = int(input('ingrese el numero del jugador: '))
        un_jugador(ingreso)


    case 3:
        nombre = input('ingrese un jugador a buscar a buscar por el nombre: ').capitalize()
        logros(nombre)

    case 4:
        alfabetico()
        

    case 5:
        nombre = input('ingrese un jugador a buscar por el nombre: ')
        salon_fama(nombre.capitalize())

    case 6:
        estadistica_mayor('rebotes_totales')

    case 7:
        estadistica_mayor('porcentaje_tiros_de_campo')

    case 8:
        estadistica_mayor('asistencias_totales')

    case 9:
        valor = input('ingrese un valor numerico: ')
        if re.match('[0-9]',valor):
            jugador_rendimiento('promedio_puntos_por_partido',int(valor))

    case 10:
        valor = input('ingrese un valor numerico: ')
        if re.match('[0-9]',valor):
            jugador_rendimiento('promedio_rebotes_por_partido',int(valor))
        
    case 11:
        valor = input('ingrese un valor numerico: ')
        if re.match('[0-9]',valor):
            jugador_rendimiento('promedio_asistencias_por_partido',int(valor))
    
    case 12:
        estadistica_mayor('robos_totales')

    case 13:
        estadistica_mayor('bloqueos_totale')

    case 14:
        valor = input('ingrese un valor numerico: ')
        if re.match('[0-9]',valor):
            jugador_rendimiento('porcentaje_tiros_libres',int(valor))
        else:
            print('no es un numero')

    case 15:
        puntos_totales()

    case 16:
        mayor_logros()

    case 17:
        valor = input('ingrese un valor numerico: ')
        if re.match('[0-9]',valor):
            jugador_rendimiento('porcentaje_tiros_triples',int(valor))
        else:
            print('no es un numero')

    case 18:
        estadistica_mayor('temporadas')

    case 19:
        valor = input('ingrese un valor numerico: ')
        if re.match('[0-9]',valor):
            orden_pisicion('porcentaje_tiros_de_campo',int(valor))

    case 21:
        cantidad_posicion()

    case 22:
        all_star()

    case 23:
        mejores_estadisticas()
    
    case 24:
        el_mejor()

    case _:
        print('Oh no °-° \nesa opcion no existe')

