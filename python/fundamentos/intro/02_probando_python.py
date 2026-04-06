import random 

"""
Este archivo sirve para practicar la ejecucion de archivos en python.
incluimos un ejemplo con un bucle y seleccion aleatoria de dias,
para que te familiarices con la termina y el flujo basico de un programa
"""

# Imprimimos un mensaje de bienvenida
print("¡Bienvenido a Python!")

# Explicamos lo que haremos a continuación
print("Ahora veremos un bucle que muestra los números del 1 al número limite que tu quieras:")

# Pide un número limite para el usuario
limitnum = int(input("Ingresa un numero: "))
# Bucle for que recorre los numeros del 1 al numero limite ingresado por el usuario
for num in range(1, limitnum + 1):
    print(f"El valor actual de num es: {num}")

# definimos una lista de dias laborales 
semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo",]

# Seleccionamos al azar un dia de la semana
dia = random.choice(semana)
print(f"Hoy es: {dia}")

# Dependiendo del dia, mostramos un mensaje motivacional distinto
if dia == "Lunes":
    print("¡Comenzamos la semana con buena energia!")
elif dia == "Viernes": 
    print("¡Cerramos la semana listos para un buen descanso!")
elif dia == "Sábado" or dia == "Domingo":
    print("¡Descansa todo lo que puedas!")
else:
    print("¡Cada dia es una nueva oportunidad de aprender!")