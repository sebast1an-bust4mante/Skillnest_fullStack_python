# Esta es la sintaxis para crear una clase llamada Usuario:


#                                       CONSTRUCTOR Y ATRIBUTOS

# ---OBJETIVOS---
# Aprender sobre los atributos de instancia
# Familiarizarse con el método __init__()
# Entender la definición de self

#Queremos que todos los usuarios que creemos tengan la misma información, 
#por ejemplo nombre, apellido, edad, correo, entre otras cosas, 
#Para esto nos ayudaremos del método constructor. 
#El método constructor es una función que contiene instrucciones para crear una  nueva instancia de la clase, 
#en este por ejemplo para crear un nuevo usuario. 
#En Python esta función se llama método  __init__ .

# Cuando llamamos a este método vamos a asignar un espacio en memoria para guardar la instancia 
# y asignarle después todos los datos correspondientes. 
# Por ejemplo:
class Usuario:
   def __init__(self): #constructor
       self.nombre = "Nariyoshi"
       self.apellido = "Miyagi"
       self.email = "miyagi@codingdojo.la"
       self.limite_credito = 30000
       self.saldo_pagar = 0

# Instancias de una clase
miyagi = Usuario()
daniel = Usuario()
sebastian = Usuario()


print(sebastian.nombre)
# Accedemos a los atributos de la instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(miyagi.apellido)
print(miyagi.email)
print(miyagi.limite_credito)
print(miyagi.saldo_pagar)

# Nuevos valores asignados a atributos de la instancia
daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "daniel@gmail.com"
daniel.limite_credito = 100000
daniel.saldo_pagar = 300000
print(daniel.nombre) #Imprime: Daniel

# Valores a nueva instancia
sebastian.nombre = "sebastian"
sebastian.apellido = "bustamante"
sebastian.email = "sebastian@gmail.com"
sebastian.limite_credito = 100000
sebastian.saldo_pagar = 300000

# Imprimir nombre de cada instancia
print(miyagi.nombre)
print(daniel.nombre)
print(sebastian.nombre)