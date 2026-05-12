class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
       self.nombre = nombre 
       self.email = email
       self.suscripcion = suscripcion
       self.lista_reproduccion = []

def agregar_a_lista(self, titulo):
       """Agrega un contenido a la lista de reproducción del usuario."""
       self.lista_reproduccion.append(titulo)
       print(f"titulo '{titulo}' agregado correctamente.") 


def ver_contenido(self, titulo):
       """Simula que el usuario reproduce un contenido."""
       if titulo in self.lista_reproduccion:
             print(f"El usuario {self.nombre} esta viendo '{titulo}'")
       else:
           print(f"Titulo no encontrado {titulo}")


def cambiar_suscripcion(self, nueva_suscripcion):
       """Cambia el tipo de suscripción del usuario."""
       susAntigua = self.suscripcion
       self.suscripcion = nueva_suscripcion
       print(f"Suscripción cambió de {susAntigua} a {nueva_suscripcion}")


def mostrar_info_usuario(self):
       """Muestra la información del usuario y su lista de reproducción."""
       print(f"Nombre: {self.nombre}")
       print(f"Email: {self.email}")
       print(f"Suscripcion: {self.suscripcion}")
       if len(self.lista_reproduccion) == 0:
           print("La lista de reproduccion está vacia.")
       else:
            print(f"Lista de reproduccion: \n- {"\n- ".join(self.lista_reproduccion)}")

#Instancias 
camilo = UsuarioStreaming("camilo")
camilo.agregar_a_lista("La casa de papel")
camilo.cambiar_suscripcion
camilo.ver_contenido
camilo.mostrar_info_usuario()