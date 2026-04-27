#                                                  MÉTODOS

# ---OBJETIVOS---
# Agregar métodos a una clase
# Comprender más profundamente el uso de self

#Los métodos son funciones que pertenecen a una clase, 
#lo que significa que no podemos llamarlos de manera independiente sino que se llaman desde una instancia

#Por ejemplo, si queremos que un usuario realice una compra con su tarjeta de crédito, 
#querríamos llamar al método desde la instancia del usuario usando notación de punto 
#sobre aquel usuario que esté realizando la compra. 
#Esa llamada se vería algo como esto:


class Usuario:
   def __init__(self, nombre, apellido, email):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = 30000
       self.saldo_pagar = 0

def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
       self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido

def aumentarCredito(self, aumento):
    self.limite_credito += aumento

def cambiarCorreo():
     
# Instancias de la clase
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")
print("------------Compras de miyagi------------")
print(miyagi.saldo_pagar) #Imprime: 450
miyagi.hacer_compra(2000)
print(f"Primera compra de {miyagi.nombre}: ${miyagi.saldo_pagar}")
miyagi.hacer_compra(300)
print(f"Segunda compra: ${miyagi.saldo_pagar}")
#Imprimir cuanto credito le queda a Miyagi
print(f"Credito disponible ${miyagi.limite_credito - miyagi.saldo_pagar}")

# Compras de Daniel 2 compras y muestra saldo a pagar ----
print("----------- Compras de daniel ------------")
daniel.hacer_compra(45)
print(daniel.saldo_pagar) #Imprime: 45

#Tarea 
'''
1.- Crear un nuevo metodo que permita aumentar el limite de credito
imprimir el nuevo limite de credito

2.- Crear un método que permita cambiar el correo de la instancia.
Mostrar el nuevo correo.
'''
miyagi.aumentarCredito(2000)
print(f"El nuevo límite de crédito es: {miyagi.limite_credito}")

miyagi.cambiarCorreo("miyagisacamela@gmail.com")
print(f"El nuevo correo establecido es: {miyagi.email}")