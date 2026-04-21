"""
Funciones básicas 1.
"""

# 1. Función que retorna la cantidad de logros desbloqueados en un videojuego.
def total_logros_desbloqueados():
    return 7

print(total_logros_desbloqueados())

# variables | valores
# a         | 10 - 4
# b         | 5 - 3
#salida: 15, 7 
# la  función genera error ya que no tiene return.

# 2. Función que indica la cantidad de mensajes enviados en un grupo de chat de tu juego online.
def mensajes_en_chat():
    return 2450

# variables | valores
# salida: ( no se imprime nada sol retorna 2450)
#

# 3. Intentamos sumar el resultado de una función que no existe al de 'mensajes_en_chat'.
print(cantidad_de_dias_en_el_anio() + mensajes_en_chat())

# variable | valores
# salida: ERROR ( NameError: cantidad_de_dias_en_el_anio no existe)
#

# Función que podría retornar la temporada en que alcanzaste un rango especial en un MOBA (por ejemplo, 2022 o 2021).
def temporada_rango_especial():
    return 2022
    return 2021  # ¿Se llega a ejecutar esta línea?

print(temporada_rango_especial())




# 4. Cantidad de listas de reproducción que sigues en una plataforma de música.
# Observa que la función 'retorna' 12, pero hay un print(15) después. ¿Se ejecuta?
def total_playlists():
    return 12
    print(15)

print(total_playlists())

# variable | valores
# salida: 2022
# el segundo return nunca se ejecuta

# 5. Función que muestra el número de episodios vistos de tu serie favorita,
# pero únicamente imprime su valor, sin retornarlo.
def episodios_serie_favorita():
    print(24)

x = episodios_serie_favorita()
print(x)

# variables | valores
# salida: 12
# el print(15) nunca se ejecuta

# 6. Función que "suma" los puntos obtenidos al compartir y al dar 'like' en una red social.
# Pero la función utiliza print en lugar de return. ¿Cómo afecta eso si queremos combinar los resultados?
def suma_puntos(a, b):
    print(a + b)

print(suma_puntos(10, 5) + suma_puntos(4, 3))

# variables | valores
# x        | None
# salida:
# 24
# None

# 7. Función para concatenar dos "tags" de redes sociales, aunque se concatenan en orden inverso.
def combinar_tags(tag1, tag2):
    return str(tag2) + str(tag1)

print(combinar_tags("#Verano", "#Diversión"))

# variables | valores
# a         | 10
# b         | 5
# salida: ERROR (TypeError por sumar None + None) 


# 8. Supongamos que 'a' representa el conteo de reproducciones de un video viral.
# Dependiendo del valor, devuelve un número distinto (p. ej., un ID de categoría).
def conteo_reproducciones_video():
    a = 560000
    print(a)
    if a < 180000:
        return 33
    else:
        return 46
    return 21  # ¿Se alcanza a ejecutar?

print(conteo_reproducciones_video())

# varible | valores
# tang1   | "#Verano"
# tang2   | "#Diversion"
# salida: #Diversion#Verano

# 9. Duración de una suscripción premium: 365 días (si se cumplen ciertas condiciones) o 12 meses.
# El tercer 'return' (52 semanas) está después del else. ¿Lo veremos?
def duracion_suscripcion(a, b):
    if a < b:
        return 365
    else:
        return 12
    return 52

print(duracion_suscripcion(1, 3))
print(duracion_suscripcion(7, 4))
print(duracion_suscripcion(7, 4) + duracion_suscripcion(1, 3))

# variables | valores
# a         | 560000
# salida:
# 560000
# 46
# el return 21 nunca se ejecuta

# 10. Suma de propinas que recibes en un juego de simulación (p.ej. "Cafetería Virtual").
# Nota que hay dos return, pero el segundo no se ejecuta nunca.
def suma_propinas(a, b):
    return a + b
    return 157

print(suma_propinas(3, 4))

# variable | valores
# a        | 1,7,7
# b        | 3,4,4
# salida:
# 365
# 12
# 377
# el return 52 nunca se ejecuta

# 11. Variable global que cuenta cuántas horas de juego llevas en total.
# Dentro de la función se define otra variable con el mismo nombre.
horas_de_juego = 150
print(horas_de_juego)

def mostrar_horas_local():
    horas_de_juego = 350
    print(horas_de_juego)

print(horas_de_juego)
mostrar_horas_local()
print(horas_de_juego)

# variable | valores
# a        | 3
# b        | 4
# salida: 7
# el return 157 nunca se ejecuta

# 12. Similar al anterior, pero la función retorna el valor local 'horas_de_juego'.
horas_de_juego = 150
print(horas_de_juego)

def mostrar_horas_local():
    horas_de_juego = 350
    print(horas_de_juego)
    return horas_de_juego

print(horas_de_juego)
mostrar_horas_local()
print(horas_de_juego)

# variables globales | valores locales | salida
#  hora_de_juego     | 150             | 150
#                    | 350 (dentro)    | 150
#                    |                 | 350
#                    |                 | 150

# 13. Ahora reasignamos la variable global con el valor que retorna la función.
horas_de_juego = 150
print(horas_de_juego)

def mostrar_horas_local():
    horas_de_juego = 350
    print(horas_de_juego)
    return horas_de_juego

print(horas_de_juego)
horas_de_juego = mostrar_horas_local()
print(horas_de_juego)

# variables globales | valores locales | salida
# horas_de_juego     | 150             | 150
#                    | 350 (dentro)    | 150
#                    |                 | 350
#                    |                 | 150

# 14. Una función que primero muestra la cantidad de seguidores en tu canal, luego llama a otra función para mostrar "Likes".
def mostrar_seguidores():
    print("Seguidores: 300")
    mostrar_likes()
    print("Finalizando conteo")

def mostrar_likes():
    print("Likes: 120")

mostrar_seguidores()

# varibles globales | valores locales | salida
# horas_de_juego    | 150             | 150 
#                   |                 | 150
#                   | 350 (dentro)    | 350
#                   | 350 (dentro)    | 350

# 15. Función que muestra "Reproducciones" de un tema musical y recibe un valor de otra función,
# luego retorna un número que podría ser un "ID" final de procesamiento.
def mostrar_reproducciones():
    print("Reproducciones: 5000")
    a = calcular_incremento()
    print(a)
    return 4

def calcular_incremento():
    print("Incremento calculado: ")
    return 1

b = mostrar_reproducciones()
print(b)

# varibles | valores
# a        | 1
# b        | 4
# salida: 5000 reproducciones, incremento calculado: 1, 4
# Finalizando conteo