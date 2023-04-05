from Orden import Orden
from Producto import Producto
from Orden import Orden
producto1 = Producto("Camisa",10.000)
producto2 = Producto("Pantalon",32456)
producto3 = Producto("Remera",1230)
producto4 = Producto("Zapato",3423)
productos1 = (producto1, producto2)
productos2 = (producto3, producto4)

orden1 = Orden(productos1)
print(orden1)
# tambien se podria añadir mas productos en una lista usando el metodo de agregar productos
# orden1.agregar_producto(producto3)
print(f"Total orden1={orden1.calculo()}")
orden2= Orden(productos2)
print(orden2)
print(f"Total orden2={orden2.calculo()}")