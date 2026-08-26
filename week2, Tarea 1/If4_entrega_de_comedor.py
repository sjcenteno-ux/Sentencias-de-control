#Un comedor realiza entrega sin recargo desde C$300. Indica si la entrega es gratuita o suma un recargo simulado de C$40.

purcharse_amount= float(input("Ingrese el monto de la compra: C$"))

if purcharse_amount >= 300:
    total= purcharse_amount
    print("Su entrega es gratuita.")

else:
    total= purcharse_amount + 40
    print("Se agrego un cargo de C$40 por la entrega")

print(f"El total a pagar es: C${total:.2f}")
print("Gracias por su compra.")