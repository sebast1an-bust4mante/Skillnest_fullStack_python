# 🚀 ¿Qué es Flask?
# Flask es un microframework para Python diseñado para crear aplicaciones web.

# Un framework es un conjunto de herramientas que facilita el desarrollo de software.

# En lugar de construir todo desde cero, Flask proporciona componentes ya preparados para desarrollar aplicaciones de forma mucho más rápida.

# Con Flask podremos:

# Crear sitios web.
# Crear sistemas de administración.
# Desarrollar APIs REST.
# Conectar aplicaciones con MySQL.
# Gestionar usuarios.
# Crear sistemas de autenticación.
# Construir aplicaciones completas.
# 🤔 ¿Por qué se llama Microframework?
# Se denomina microframework porque incluye únicamente las herramientas esenciales para crear aplicaciones web.

# Esto significa que:

# Es ligero.
# Es sencillo de aprender.
# Es muy flexible.
# Podemos agregar únicamente las herramientas que realmente necesitamos.
# A diferencia de otros frameworks más grandes, Flask no obliga al desarrollador a seguir una estructura específica.

# 🌎 ¿Qué es una aplicación web?
# Una aplicación web es un programa que funciona desde un navegador.

# Algunos ejemplos conocidos son:

# Gmail
# Facebook
# Instagram
# YouTube
# Mercado Libre
# BancoEstado en Línea
# Todas estas aplicaciones reciben solicitudes del usuario, procesan información en un servidor y devuelven una respuesta al navegador.

# Eso mismo aprenderemos a construir con Flask.

'''
Importante: Flask no reemplaza los conocimientos de Python. 
Todo lo que has aprendido hasta ahora seguirá siendo utilizado constantemente durante este curso.
'''

#------------------------------------------------------------
#🐍 Python
#Python será el lenguaje principal del servidor.

#Toda la lógica de negocio seguirá siendo escrita en Python.
#------------------------------------------------------------

#Ejemplo:

nombre = "Daniel"

if nombre == "Daniel":
    print("Bienvenido")

#🔤 Variables
#Las variables almacenan información.

nombre = "Carlos"
edad = 25
activo = True

#📋 Listas
#Nos permiten almacenar múltiples elementos.

productos = [
    "Notebook",
    "Mouse",
    "Teclado"
]

#🔁 Bucles
#Permiten recorrer colecciones de datos.

for producto in productos:
    print(producto)

#🔀 Condicionales
#Permiten tomar decisiones.

edad = 18

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

#🛠 Funciones
#Nos ayudan a reutilizar código.

def saludar(nombre):
    return f"Hola {nombre}"

#------------------------------------------------------------
#🧩 Componentes que utilizaremos durante el curso
#Durante las próximas unidades aprenderemos a trabajar con los siguientes componentes.
#------------------------------------------------------------

# 🖼 Renderizado de Plantillas
# Permite enviar archivos HTML al navegador.

# Flask utiliza la función:
#render_template()

# Ejemplo:

#return render_template("index.html")
# Gracias a esto podremos separar la lógica del programa (Python) de la interfaz del usuario (HTML).

# ↪ Redirecciones
# Permiten enviar automáticamente al usuario hacia otra página.

# Ejemplo:

#return redirect("/dashboard")
# Esto suele utilizarse después de:

# Iniciar sesión.
# Guardar un formulario.
# Actualizar un registro.
# Eliminar información.
# 📝 Formularios
# Los formularios permiten que los usuarios envíen información al servidor.

# Ejemplo:

# <form action="/guardar" method="POST">

#     <input
#         type="text"
#         name="nombre"
#     >

#     <button>Guardar</button>

# </form>
# Cada vez que un usuario escribe información y presiona un botón, el formulario envía esos datos hacia Flask.

# 🔍 Solicitudes HTTP
# La comunicación entre un navegador y un servidor se realiza mediante solicitudes HTTP.

# Las dos más importantes serán:

# GET
# Se utiliza para solicitar información.

# Ejemplo:

# GET /productos
# Generalmente se utiliza para:

# Ver páginas.
# Buscar información.
# Mostrar registros.
# POST
# Se utiliza para enviar información.

# Ejemplo:

# POST /usuarios
# Generalmente se utiliza para:

# Registrar usuarios.
# Iniciar sesión.
# Guardar formularios.
# Actualizar datos.
# 🔐 Sesiones
# Las sesiones permiten recordar información del usuario mientras navega por el sistema.

# Por ejemplo:

# session["usuario"] = "Carlos"
# Gracias a las sesiones podremos saber:

# Quién inició sesión.
# Qué permisos tiene.
# Qué productos tiene en un carrito de compras.