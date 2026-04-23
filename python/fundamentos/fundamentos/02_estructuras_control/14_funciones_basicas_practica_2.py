import os
#Ejercicio 1-----------------------------------
#
# Calcula experiencia
def multiplica_por_2():
  for i in range(0, 12, 2):
    if(i % 2 == 0):
     def ejercicio1():
      resultado1 = multiplica_por_2(5)
# Debe retornar: [0, 2, 4, 6, 8, 10]

#Ejercicio 2-----------------------------------
# Analiza publicaciones
def suma_y_resta(list):
    suma = list[0] + list[1]
    resta = list[0] - list[1]
    print(f"suma : {suma}")
    return resta
def ejercicio2():
  resta = suma_y_resta([120, 115])
  print(f"retorno / resta; {resta}")
# Imprime: 235 y retorna: 5

#Ejercicio 3-----------------------------------
# Puntaje ajustado
def sumatoria_menos_longitud(sumatoria):
    total = sum(sumatoria)
    longitud = len(sumatoria)
    resultado = total - longitud
    return resultado
def ejercicio3():
  retornar = sumatoria_menos_longitud([10, 5, 3, 7])
  print(f"El resultado del retorno es: {retornar}")
# Suma total = 25, longitud = 4, debe retornar: 21

#Ejercicio 4-----------------------------------
# Ajusta visualizaciones
def valores_multiplicados_segundo(lista):
  if len(lista) < 2:
    print(len(lista))
    return []
  else:
    segEle = lista[1]
    nuevaLista = []
    for i in lista:
      nuevaLista.append(i * segEle)
    long = len(nuevaLista)
    print(long)
    return 
def ejercicio4():
  result1 = valores_multiplicados_segundo([100, 3, 50, 20])
  print(result1)
  print()
# Imprime: 4 y retorna: [300, 9, 150, 60]
  result2 = valores_multiplicados_segundo([100])
  print(result2)

#Ejercicio 5-----------------------------------
def valores_multiplicados_longitud(a, b):
  multList = []
  for i in range(0, b):
    multList.append(a * b)
    return multList
def valores_multiplicados_segundo():
  result1 = valores_multiplicados_longitud(5, 2)
  print(f"Resultado 1: {result1}")
  # Debe retornar: [10, 10]
  result2 = valores_multiplicados_longitud([100])
  print(f"Resultado 2: {result2}")
# Imprime: 1 y retorna: []

def limpiar_consola():
  os.system('')

continuar = True
while continuar:
  print("\n--- Ejercicios Python ---")
  print("--- 1.- Ejercicio 1 ---")
  print("--- 2.- Ejercicio 2 ---")
  print("--- 3.- Ejercicio 3 ---")
  print("--- 4.- Ejercicio 4 ---")
  print("--- 5.- Ejercicio 5 ---")
  opcion = input("\n---- Elige una opción: (1-15) (0 para salir) =")
  if opcion == "1":
    print("\nEjecutando ejercicio 1: ")
    print(multiplica_por_2())
  elif opcion == "2":
    print("\nEjecutando ejercicio 2: ")
    print(suma_y_resta())
  elif opcion == "3":
    print("\nEjecutando ejercicio 3: ")
    print(sumatoria_menos_longitud())
  elif opcion == "4":
    print("\nEjecutando ejercicio 4: ")
    print(valores_multiplicados_segundo())
  elif opcion == "5":
    print("\nEjecutando ejercicio 5: ")
    print(valores_multiplicados_longitud())
