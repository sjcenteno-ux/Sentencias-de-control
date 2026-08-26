#Una distribuidora revisa 8 productos. Solicita nombre y existencia;
#muestra los que tienen menos de 10 unidades y cuenta las alertas.

alert_acount= 0
for product in range (1, 9):
 product_name= input("Ingrese el nombre del producto:")
 stock= int(input("Ingrese la cantidad del producto:"))

 if stock < 10:
  print(f"ALERTA: El producto {product} tiene menos de 10 unidades.")
  alert_acount = alert_acount + 1


print(f"El total de alertas fueron: {alert_acount }")