#Ingresa los montos de ventas hasta escribir 0. Calcula el total recaudado y la cantidad de ventas.

total_sales= 0
sales_count= 0

sale= float(input("Ingrese la primera venta:"))

while sale != 0:
    total_sales = total_sales + sale
    sales_count = sales_count + 1

    sale = float(input("Ingresa el monto de la venta (0 para finalizar): "))

    
print(f"Total recaudado: C${total_sales:.2f}")
print(f"Cantidad de ventas: {sales_count}")
