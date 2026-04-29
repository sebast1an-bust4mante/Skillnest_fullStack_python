#                                        REQUISITOS OBLIGATORIOS
#Su trabajo debe cumplir con lo siguiente:
# Uso de funciones con parámetros
# Uso de menú con ciclo while
# Uso de input() para solicitar datos
# Uso de listas (arreglos)
# Uso de diccionarios
# Uso de ciclos for
# Uso de estructuras condicionales (if, elif, else)
# Código ordenado, comentado y correctamente indentado
# Opción de salida del programa (0. Salir)

#                                        EJERCICIOS A DESARROLLAR
#Su programa deberá considerar las siguientes funciones:

# 1.- Crear una función que reciba una lista de números enteros y muestre cuál es el número mayor 
# y cuál es el menor.
def numeroMayorMenor(listado):
    menor = min(listado)
    mayor = max(listado)
    print(f"El número nayor es {mayor}\nEl número menor es: {menor}")

def ejercicio1():
    limit = int(input("Ingresa un limite de valores: "))
    listadoNum = []
    i = 1
    while i <= limit:
        num = input("Ingresa un número entero: ")
        listadoNum.append(num)
        i+=1
    numeroMayorMenor(listadoNum)


# 2.- Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene.
def contador_vocal(letra):
    return letra in vocales # Devuelve True si la letra está adentro de las vocales, 

def contar_vocales(texto):
    contador = 0
    for letra in texto:
        if es_vocal(letra):
            contador += 1
    print(f"La cadena contiene {contador}")

# 3.- Crear una función que reciba una lista de nombres y muestre únicamente aquellos que 
# tengan más de 5 letras.


# 4.- Crear una función que reciba una lista de notas (números decimales), 


# calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).


# 5.- Crear una función que reciba una lista de precios de productos y 
# aplique un descuento del 10%, mostrando el valor original y el nuevo valor.


# 6.- Crear una función que reciba un número entero y determine si es par o impar.


# 7.- Crear una función que reciba una lista de edades y muestre cuántas personas 
# son mayores de edad (18 años o más).


# 8.- Crear una función que reciba una lista de palabras y permita buscar cuántas veces 
# aparece una palabra específica ingresada por el usuario.


# 9.- Crear una función que reciba una lista de números 
# y genere una nueva lista que contenga únicamente los números positivos.


# 10.- Crear una función que reciba una lista de productos (utilizando diccionarios con nombre y stock) 
# y muestre cuáles tienen un stock menor a 5 unidades.
