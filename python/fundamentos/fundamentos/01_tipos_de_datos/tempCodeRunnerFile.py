num1 = int(input("Ingresar primer número: "))
num2 = int(input("Ingresar segundo número: "))
num3 = int(input("Ingresar tercer número: "))

# Detectar menor
numeros = num1, num2, num3
mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")