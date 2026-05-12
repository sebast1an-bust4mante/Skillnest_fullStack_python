#Atributos; métodos de clase, metodos estáticos

#                                        DEFINICION DE LA CLASE
class Estudiante:
    #Atributo de Clase
    colegio = "Liceo Vate Vicente Huidobro"
    #Lista en donde esten todos los estudiantes
    estudiantes = []

    #Método CONSTRUCTOR
    def __init__(self, nombre, nota):
        #Atributos de instancia
        self.nombre = nombre
        self.nota = nota
        #Agregar elementos a lista estudiante (objeto)
        Estudiante.estudiantes.append(self)

    #Método de instancia
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}") 

    # Uso de métodos de instancia
    print("== MÉTODO DE INSTANCIA==")
    #Mostrar datos de estudiantes
    def mostrar_info(self):
        e1.mostrar_info() 
        e2.mostrar_info()

    #Usar atributos de clase
    print("== ATRIBUTO DE CLASE ==")
    print(e1.colegio)
    print(e2.colegio)

    #Uso de método de clase
    print("=== MÉTODO DE CLASE ===")

    Estudiante.cambiar_colegio("Purkuyen")
    print(e1.colegio)
    print(e2.colegio)
    print()

    #Contar Estudiantes
    print("=== CONTAR ESTUDIANTES ===")
    print(f"Total estudiantes: {Estudiante.cantidad_estudiantes()}")
    
    #Método estático
    print("=== MÉTODO ESTÁTICO ===")

    print(f"¿{e1.nombre} Aprueba?")
    print(Estudiante.aprobar)
    print()

    print(f"¿{e2.nombre} Aprueba?")
    print(Estudiante.aprobar)
    print()

    print(f"¿{e3.nombre} Aprueba?")
    print(Estudiante.aprobar)
    print()

    #DEFINICION DE CLASE

    #Método de CLASE
    # Usa "CLS" porque trabaja con la información de la clase
    @classmethod
    def cambiar_colegio(cls, nuevo_nombre):
        cls.colegio = nuevo_nombre

    @classmethod #Contar la cantidad de estudiantes existentes
    def cantidad_estudiantes(cls):
        return len(cls.estudiantes)
    
    #Método estático
    #Este no usa CLS ni self, solo parámetros.
    @staticmethod
    def aprobar(nota):
        if nota >= 4.0:
            return True
        else:
            return False
        
#Creación de Objetos
e1 = Estudiante("Donovan" 4.0)
e2 = Estudiante("Randy", 6.7)
e3 = Estudiante("Martin", 3.9)

## Función repaso
## Crear una función que valide usuario y contraseña

def validador(user, password):
    if user == "matias123" and password == "matias123":
        print(f"Bienvenido,, {user}!")
        return True
    else:
        print("Acceso Denegado")
        return False
    
def enviarDatos():
    username = input("Ingrese su nombre usuario: ")
    password = input("Ingrese su contraseña: ")
    validador(username, password)

enviarDatos()