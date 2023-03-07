# -*- coding: utf-8 -*-

def sumar_tiempos(tiempo1, tiempo2):
    # Convertir los tiempos en segundos
    segundos1 = tiempo1[0] * 60 + tiempo1[1]
    segundos2 = tiempo2[0] * 60 + tiempo2[1]
    # Sumar los segundos
    segundos_totales = segundos1 + segundos2
    # Convertir los segundos totales en minutos y segundos
    minutos_totales, segundos_totales = divmod(segundos_totales, 60)
    # Retornar el resultado como una tupla
    return (minutos_totales, segundos_totales)

# Pedir los tiempos por entrada de datos
tiempos_str = input("Intoduzca los tiempos a sumar (en formato minutos:segundos separados por '+'):\n\n")
# Separar los tiempos por el signo '+'
tiempos_list = tiempos_str.split("+")
# Inicializar los minutos y segundos totales en 0
minutos_totales = 0
segundos_totales = 0
# Recorrer la lista de tiempos y sumar los minutos y segundos
for tiempo in tiempos_list:
    # Separar los minutos y segundos de cada tiempo y convertirlos a enteros
    try:
        minutos, segundos = map(int, tiempo.split(":"))
    except ValueError:
        print(f"Error: el tiempo '{tiempo}' no tiene el formato correcto (minutos:segundos).")
        exit()
    # Verificar que los minutos y segundos estén dentro del rango permitido
    if minutos < 0 or minutos > 59:
        print(f"Error: el tiempo '{tiempo}' tiene un valor de minutos invalido.")
        exit()
    if segundos < 0 or segundos > 59:
        print(f"Error: el tiempo '{tiempo}' tiene un valor de segundos invalido.")
        exit()
    # Sumar los minutos y segundos totales
    minutos_totales += minutos
    segundos_totales += segundos
# Sumar los minutos y segundos totales y convertirlos en minutos y segundos
minutos_totales += segundos_totales // 60
segundos_totales %= 60

# Mostrar el resultado
print(f"\nEl resultado de la suma es: {minutos_totales} minutos y {segundos_totales} segundos.")
