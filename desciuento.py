
class Producto:
    """
    Clase para crear objetos tipo Producto
    """
    
    def __init__(self, nombre, precio):
        """
        Inicializamos el constructor
        """
        self.nombre = nombre  #inicializamos la variable nombre
        self.precio = precio  #inicializamos la variable precio


    def aplicar_descuento (self,porcentaje):
         """
         Metodo para aplicar un descuento.
         Parametros:
         self (str): El nombre del producto.
         porcentaje (double): porcentaje a aplicar
         """

         descuento=self.precio * (porcentaje / 100) #realiza operacion
         self.precio -= descuento  #asignamos el valor a self.precio
    

    def mostrar_informacion (self):
         """
         Metodo para mostrar la información en consola
         """
         print(f"Producto: {self.nombre}")
         print(f"Precio actual: $ {self.precio:.2f}")




 #creacion de interaccion con el objeto
producto1= Producto("Jamon", 55.00)
producto1.aplicar_descuento(25)    #Aplicar un 25 porciento de descuento
producto1.mostrar_informacion()  #imprime informacion actualizada
