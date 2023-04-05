from Producto import Producto

class Orden:
    contador_ordenes = 0
    def __init__(self, producto):
       Orden.contador_ordenes += 1
       self._Id_orden = Orden.contador_ordenes
       self._producto = list(producto)

    def agregar_producto(self,producto):
     self._producto.append(producto)

    def calculo(self):
        total = 0
        for producto in self._producto:
          total += producto._precio
        return total

    def __str__(self):
       producto_str=""
       for producto in self._producto:
           producto_str += producto.__str__() + "|"

       return f"Orden:{self._Id_orden}, Producto:{producto_str}"

if __name__: "__main__"

