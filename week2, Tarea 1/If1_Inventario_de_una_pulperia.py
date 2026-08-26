#Inventario de una pulpería
#La pulpería La Esquina necesita reponer un producto cuando quedan menos de 5 unidades. 
#Solicita el nombre y la existencia; muestra una alerta cuando corresponda.

product_name= input("Ingrese el nombre del producto:")
stock= int(input("Ingrese la existencia del producto:"))


if stock <5:
    print(f"ALERTA: Debe reponer el producto{product_name}.")
else:
    print("Cantidad suficiente.")