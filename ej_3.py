# Crear una función que reciba una lista de notas (decimales) y genere dos listas: 
# una con aprobados (≥ 4.0) y otra con reprobados (< 4.0).
# Debe mostrar ambas listas y la cantidad de estudiantes en cada grupo.
def revisarNotas(lista):
    aprobados = []
    reprobados = []
    for i in range(0, len(lista)):
        if lista[i] < 4.0:
            reprobados.append(str(lista[i]))
        else:
            aprobados.append(str(lista[i]))
    print(f"\nalumnos reprobados: {len(reprobados)}\nnotas: {" - ".join(reprobados)}")
    print(f"alumnos aprobados: {len(aprobados)}\nnotas: {" - ".join(aprobados)}")

def ejercicio2():
    limite = int(input("Ingrese un limite de notas: "))
    listaNotas = []
    i = 0
    while i < limite:
        nota = float(input("Ingrese la nota de un estudiante: "))
        if nota < 1.0 or nota > 7.0:
            print("Nota inválida")
        else: 
            print("Nota agregada con éxito")
            listaNotas.append(nota)
            i += 1
    revisarNotas(listaNotas)
ejercicio2() 