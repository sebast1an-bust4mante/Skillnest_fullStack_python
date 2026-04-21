while condicion:
   #Código que se ejecuta mientras la condición se cumpla

   num = 0

while num < 4:
   print("bucle while -", num)
   num += 1
#Imprime: bucle while - 0, bucle while - 1, bucle while - 2, bucle while - 3

num = 0
while num < 4:
   print("bucle while -", num)
   num += 1
else:
   print("Acabamos de salir del bucle")

#Break
# La sentencia break termina de forma definitiva el bucle y 
# continúa con la primera sentencia después del bucle.
for letra in "detente":
   if letra == "n":
       break
   print(letra)
#Imprime: d, e, t, e

#Continue
# La sentencia continue regresa el control al comienzo del bucle; 
# de alguna manera a través de continue podemos “saltar” 
# todas las sentencias restantes
for letra in "detente":
   if letra == "n":
        continue
   print(letra)
#Imprime: d, e, t, e, t, e

# En el ejemplo anterior, “saltamos” la letra n, 
# pero nuestro bucle continuó funcionando de manera normal.
# Observa el comportamiento del "else" acompañado de una sentencia "break"
x = 6
while x > 2:
   print(x)
   x -= 1
   if x == 3:
       break
else: #Recuerda: Solo se ejecuta en una salida normal, NO en un break
   print("Sentencia final")