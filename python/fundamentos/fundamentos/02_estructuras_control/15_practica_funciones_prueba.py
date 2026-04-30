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
def filtrar(lista):
    resultado = []
    for nombre in lista:
        if len(nombre) > 5:
            resultado.append(nombre)
        return resultado
    
def mostrar():
    nombres = []

for i in range():
    nombre = input("Ingrese un nombre: ")
    print(f"{nombre}")

# 4.- Crear una función que reciba una lista de notas (números decimales), 
def listaNotas(notas):
    lista = 0
    for i in range(len(notas)):
        lista += notas[i]
    promedio = lista / (len(lista) + 1)

    if notas[i] >= 4.0 and notas[i] <= 7.0:
        return f"El estudiante {i + 1} pasa con un {promedio}"
    elif notas[i] >= 1 and notas[i] <= 3.9:
        return f"El estudiante {i + 1} no pasa con un {promedio}"
    else:
        return "Error"
    
def ejercicio4():
    largo = int(input("Cuantas notas va a ingresar: "))
    nota = [] # nota es una lista
    for i in range(largo): # el "for" almacena las notas, ejecutando un bucle con un limite
        inp = float(input(f"Ingrese nota {i + 1}: "))
        if inp != "": # validacion, si "input" es distinto a vacio, inserta "inp" a nota con ".append"
            nota.append(inp) # 
        print(listaNotas(nota)) # Arreglo
ejercicio4() # llama la funcion "ejercicio4", osea que el codigo se ejecuta de "ejercicio4"

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
