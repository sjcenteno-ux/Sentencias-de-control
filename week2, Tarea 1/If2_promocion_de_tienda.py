#Una tienda de Masaya aplica una promoción simulada de 10% cuando la compra supera C$1,500. Solicita el monto y muestra el total.
purcharse_amount= float(input("Ingrese el monto de la compra: C$"))
discount= 0

if purcharse_amount > 1500:
    discount= purcharse_amount * 0.10

total= purcharse_amount - discount

print(f"El total a pagar es de: {total:.2f}")

print("Gracias por su compra.")