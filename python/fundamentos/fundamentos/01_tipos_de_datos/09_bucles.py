# Bucles python

# For in range
for i in range(2, 8):
   print(i)

for i in range(0, 15, 3):
   print(i)
#Imprime: 0, 3, 6, 9, 12

for i in range(10, 1, -3):
   print(i)
#Imprime: 10, 7, 4

# Recorrer un string
for letra in 'Python':
   print(letra)
#Imprime: 'P', 'y', 't', 'h', 'o', 'n'

lista = ['brócoli', 'pepino', 'pimiento']

for i in range( len(lista) ):
   print(i, lista[i])
#Imprime: 0 brócoli, 1 pepino, 2 pimiento

for verdura in lista:
   print(verdura)
#Imprime: brócoli, pepino, pimiento

tupla = ('fresa', 'manzana', 'cereza')

for i in range( len(tupla) ):
   print(i, tupla[i])
#Imprime: 0 fresa, 1 manzana, 2 cereza

for fruta in tupla:
   print(fruta)
#Imprime: fresa, manzana, cereza

estudiante = {"nombre": "Gonzalo", "curso": "Python"}

for clave in estudiante:
   print(clave)
#Imprime: nombre, curso

estudiante = {"nombre": "Gonzalo", "curso": "Python"}

for clave in estudiante:
   print(estudiante[clave])
#Imprime: Gonzalo, Python

# Ejemplo de recorrido de un diccionario de platillos tipicos-----------------------
platillos_tipicos = {"México": "Tacos", "Colombia": "Ajiaco", "Costa Rica": "Casado"}

#Otra forma de iterar a través de las claves
for clave in platillos_tipicos.keys():
   print(clave)
#Imprime: México, Colombia, Costa Rica

#Iteramos a través de los valores
for valor in platillos_tipicos.values():
   print(valor)
#Imprime: Tacos, Ajiaco, Casado

#Iteramos a través de los elementos (clave-valor)
for clave, valor in platillos_tipicos.items():
   print(clave, "=", valor)
#Imprime: México = Tacos, Colombia = Ajiaco, Costa Rica = Casado
# -----------------------------------------------------------------------------------------------------------------------------
# Range con 1 argumento
for i in range(4): # lo que esta dentro del parentesis es el argumento y se suma en 1 hasta llegar al 3 porque (4) es el limite
   print(i)
#Imprime 1, 2, 3

# Range con 2 argumentos
for i in range(2, 8): # el segundo numero (8) siempre sera el tope y el primero el numero inicial (2) 
   print(i)
#Imprime 2, 3, 4, 5, 6, 7

# Range con 3 argumentos
for i in range(2, 10, 3): #el tercer numero hara que el 2 suba de 3 en 3 siendo 10 el top
   print(i)
#Imprime 2, 5, 8

#  En caso de necesitar un paso para nuestra secuencia, es necesario enviar los tres argumentos al rango. 
# ¡Los rangos también pueden ser decrementales! 
# Para lograr esto, indicaremos que el paso sea un número negativo.
for i in range(0, 15, 3):
   print(i)
#Imprime: 0, 3, 6, 9, 12

for i in range(10, 1, -3):
   print(i)
#Imprime: 10, 7, 4

# Recorrer cadenas con bucles for
for letra in 'Python':
   print(letra)
#Imprime: 'P', 'y', 't', 'h', 'o', 'n'

# Recorrer listas con bucles for
lista = ['brócoli', 'pepino', 'pimiento']

for i in range( len(lista) ): # len es length, osea el ancho 
   print(i, lista[i])
#Imprime: 0 brócoli, 1 pepino, 2 pimiento

for verdura in lista:
   print(verdura)
#Imprime: brócoli, pepino, pimiento

# Recorrer tuplas con bucles for
tupla = ('fresa', 'manzana', 'cereza')

for i in range( len(tupla) ):
   print(i, tupla[i])
#Imprime: 0 fresa, 1 manzana, 2 cereza

for fruta in tupla:
   print(fruta)
#Imprime: fresa, manzana, cereza

# Recorrer diccionarios con bucles for
estudiante = {"nombre": "Gonzalo", "curso": "Python"}

for clave in estudiante:
   print(clave)
#Imprime: nombre, curso

# Ya tenemos las claves, ahora ¿cómo accedemos al valor? 
# ¡Colocando la clave entre corchetes! Veamos:
estudiante = {"nombre": "Gonzalo", "curso": "Python"}

for clave in estudiante:
   print(estudiante[clave])
#Imprime: Gonzalo, Python

# En el capítulo de diccionarios vimos algunos métodos que nos permitían obtener 
# las secuencias con los valores, claves y elementos de un diccionario. 
# Prueba el siguiente fragmento de código para ver su funcionamiento en acción:
platillos_tipicos = {"México": "Tacos", "Colombia": "Ajiaco", "Costa Rica": "Casado"}

#Otra forma de iterar a través de las claves
for clave in platillos_tipicos.keys():
   print(clave)
#Imprime: México, Colombia, Costa Rica

#Iteramos a través de los valores
for valor in platillos_tipicos.values():
   print(valor)
#Imprime: Tacos, Ajiaco, Casado

#Iteramos a través de los elementos (clave-valor)
for clave, valor in platillos_tipicos.items():
   print(clave, "=", valor)
#Imprime: México = Tacos, Colombia = Ajiaco, Costa Rica = Casado