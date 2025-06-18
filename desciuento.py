 #este codigo que eh desarrollado es una aplicación simple 

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio =precio

    def aplicar_descuento (self,porcentaje):
         descuento=self.precio * (porcentaje / 100)
         self.precio -= descuento
    
    def mostrar_informacion (self):
         print(f"Producto: {self.nombre}")
         print(f"Precio actual: $ {self.precio:.2f}")


 #creacion de interaccion con el objeto
producto1= Producto("Jamon", 55.00)
producto1.aplicar_descuento(25)    #Aplicar un 25 porciento de descuento
producto1.mostrar_informacion()  #imprime informacion actualizada
