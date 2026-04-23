# Ranking de puntajes de un torneo de eSports
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]


# Lista de creadores de contenido en una plataforma de streaming
streamers = [
   {"nombre": "GameNinjaPro", "seguidores": 250000},
   {"nombre": "PixelWarrior", "seguidores": 180000}
]


# Eventos en distintas ciudades del mundo
eventos = {
   "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
   "España": ["Madrid", "Barcelona", "Valencia"]
}


# Coordenadas de la sede de un torneo internacional
ubicacion = [
   {"latitud": 34.052235, "longitud": -118.243683}
]

# En puntajes, cambia el valor 300 por 600 (ajuste en los puntajes de la primera ronda). Resultado esperado:
# puntajes = [[1000, 1500, 2000], [600, 700, 1400]]

#1. cambiar 300 por 600 
puntajes[1][0] = 600
print(puntajes)

#2. Cambiar "Gameninjapro" por "EliteGamerx"
streamers[0]["nombre"] = "ElitegamerX"
print(streamers)

#3. Cambiar "Las vegas " por "San Fransico"
eventos["Estados unidos"][2] = "San Fransisco"
print(eventos)

#4. Cambiar Lotitud a 40.712776
ubicacion[0]["Lotitud"] = 40.712776
print(ubicacion)

def iterar_diccionario(lista):
    for diccionario in lista:
        for clave, valor in diccionario.items():
            print(f"{clave} - {valor}")

def obtener_valores(clave, lista):
    for diccionario in lista:
        print(diccionario[clave])

# Valores
obtener_valores("nombre", streamers) 
obtener_valores("seguidores", streamers)

def mostrar_informacion(diccionario):
   for clave in diccionario:
      lista = diccionario[clave]
      print(f"{len(lista)} {clave.upper()}")
      for elemento in lista:
         print(elemento)
         print()

# Datos
datos = {
   "juegos_populares": [
      "Fortnite", 
      "Minecraft", 
      "Valorant", 
      "GTA V",
   ],
   "ciudades_eventos": [
      "Nueva York",
      "Madrid",
      "Tokio",
   ]
}

mostrar_informacion(datos)