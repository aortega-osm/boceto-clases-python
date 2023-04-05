class Producto:
    cuentaProducto=0
    def __init__(self,nombre,precio):
            Producto.cuentaProducto +=1
            self.Id=Producto.cuentaProducto
            self._nombre=nombre
            self._precio=precio

    @property
    def nombre(self):
            return self._nombre

    @nombre.setter
    def nombre(self,nombre):
            self._nombre=nombre
    @property
    def precio(self):
            return  self._precio

    @precio.setter
    def precio(self,precio):
            self._precio=precio

    def __str__(self):
        return (f"[Id producto:{self.Id}],[Nombre:{self._nombre}],[Precio:{self._precio}]")

#
producto1=Producto("Camisa",10.000)
# print(producto1)
producto2=Producto("Pantalon",32456)
# print(producto2)

