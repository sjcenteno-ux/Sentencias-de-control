#Una cooperativa recibe 5 sacos. Solicita el peso de cada uno, muestra su número de recepción y calcula el peso total.
total_weight= 0

for bag in range (1, 6):
    weight= float(input(f"Ingrese el peso del saco numero {bag}:KG"))
    total_weight= weight + total_weight
    print(f"Saco {bag} recibido")
    print(f"El peso total es de:{total_weight:.2f}")