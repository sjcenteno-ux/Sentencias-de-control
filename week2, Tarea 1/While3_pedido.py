#Un distribuidor acepta de 1 a 100 unidades. 
# Solicita la cantidad hasta que sea válida y luego calcula el total.

unit_price= 25

quantity= int(input("Ingrese la cantidad de unidades. (solo se aceptan del 1 al 100.): "))

while quantity < 1 or quantity > 100:
    print("Cantidad invalida.")
    quantity= int(input("Ingrese nuevamente la cantidad de unidades:"))


total= quantity * unit_price

print (f"Cantidad valida: {quantity} unidades.")
print (f"Total a pagar: C${total:.2f}")