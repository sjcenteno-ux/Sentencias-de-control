#Una tienda tiene 3 unidades y desea llegar a 20.
#  Solicita cada reposición y termina al alcanzar o superar la meta.

stock = 3

while stock < 20:
    restock= int(input("Ingrese la cantidad a reponer: "))

    if restock >0:
        stock = stock + restock 
        print(f"Existencia actual: {stock}")



    else:
      print("Cantidad inválida. Debe ingresar una cantidad mayor que 0.")

print(f"Meta alcanzada. Existencia final: {stock} unidades.")