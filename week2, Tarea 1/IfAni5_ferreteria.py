# Una ferretería distingue mayoristas y minoristas. Para cada tipo, el descuento depende de un monto mínimo diferente.
# Propón porcentajes y explica tus reglas
print("Si el cliente es mayorista y su compra es de un minimo de C$3000, se le aplicara un descuento del 15%")
print("Si el cliente es minorista y su compra es de un minimo de C$ 1500, se le aplicara un descuento del 8%")
print("Independientemente del tipo del cliente si no alcanza su minimo de monto, no se le aplicara descuento.")

customer_type= input ("Ingrese el tipo de cliente: mayorista/minorista.")
purcharse_amount= float(input("Ingrese la cantidad de la compra:"))
discount= 0

if customer_type.lower() == "mayorista":
    if purcharse_amount >=3000:
        discount= purcharse_amount * 0.15


else:
    if purcharse_amount >=1500:
        discount = purcharse_amount * 0.08

total= purcharse_amount - discount
print(f"El descuento aplicado es de: C${discount:.2f}")
print(f"El total a pagar es de: C${total:.2f}")
    
