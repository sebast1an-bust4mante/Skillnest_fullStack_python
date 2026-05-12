class SuscripcionStreaming:
    costos = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}

    def __init__(self, usuario, tipo_suscripcion="Gratis"):
        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = self.costos[tipo_suscripcion]
        self.saldo_pendiente = self.costo_mensual

    def realizar_pago(self, monto):
        if monto <= 0:
            print("El monto debe ser mayor a 0.")
            return
        if monto >= self.saldo_pendiente:
            print(f"{self.usuario} pagó ${monto}. Saldo restante: $0.00")
            self.saldo_pendiente = 0
        else:
            self.saldo_pendiente -= monto
            print(f"{self.usuario} pagó ${monto}. Saldo restante: ${self.saldo_pendiente:.2f}")

    def cambiar_suscripcion(self, nuevo_tipo):
        if nuevo_tipo in self.costos:
            self.tipo_suscripcion = nuevo_tipo
            self.costo_mensual = self.costos[nuevo_tipo]
            self.saldo_pendiente += self.costo_mensual
            print(f"{self.usuario} cambió a {nuevo_tipo}.")
        else:
            print(f"Error: '{nuevo_tipo}' no es un plan válido.")

    def ver_contenido_exclusivo(self):
        if self.tipo_suscripcion == "Gratis":
            print(f"{self.usuario} no puede ver contenido exclusivo.")
        else:
            print(f"{self.usuario} está viendo contenido exclusivo.")

    def mostrar_info_suscripcion(self):
        print(f"{self.usuario} | Plan: {self.tipo_suscripcion} | Deuda total: ${self.saldo_pendiente:.2f}")


# Instancias
u1 = SuscripcionStreaming("Ana", "Gratis")
u2 = SuscripcionStreaming("Carlos", "Estándar")
u3 = SuscripcionStreaming("Beatriz", "Premium")

print("\n--- Pruebas Usuario 1 ---")
u1.ver_contenido_exclusivo()
u1.cambiar_suscripcion("Estándar")
u1.realizar_pago(5.99)

print("\n--- Pruebas Usuario 2 ---")
u2.ver_contenido_exclusivo()
u2.cambiar_suscripcion("Premium")
u2.realizar_pago(10.00)
u2.realizar_pago(6.98)

print("\n--- Pruebas Usuario 3 ---")
u3.realizar_pago(5.00)
u3.ver_contenido_exclusivo()

print("\n--- Resumen Final ---")
u1.mostrar_info_suscripcion()
u2.mostrar_info_suscripcion()
u3.mostrar_info_suscripcion()