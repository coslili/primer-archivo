class Producto:
    """
    Clase base para crear objetos tipo Producto
    """
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        """
        Aplica un descuento al precio del producto.
        """
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento

    def mostrar_informacion(self):
        """
        Muestra la información del producto.
        """
        print(f"Producto: {self.nombre}")
        print(f"Precio actual: $ {self.precio:.2f}")

# Subclase para productos alimenticios
class ProductoAlimenticio(Producto):
    def __init__(self, nombre, precio, fecha_caducidad):
        super().__init__(nombre, precio)  # reutilizamos el constructor de la clase base
        self.fecha_caducidad = fecha_caducidad

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Fecha de caducidad: {self.fecha_caducidad}")

# Subclase para productos electrónicos
class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, garantia_meses):
        super().__init__(nombre, precio)
        self.garantia_meses = garantia_meses

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Meses de garantía: {self.garantia_meses}")


producto1 = ProductoAlimenticio("Jamon", 55.00, "2025-12-31")
producto1.aplicar_descuento(25)
producto1.mostrar_informacion()

print()

producto2 = ProductoElectronico("Televisor", 1200.00, 24)
producto2.aplicar_descuento(10)
producto2.mostrar_informacion()
