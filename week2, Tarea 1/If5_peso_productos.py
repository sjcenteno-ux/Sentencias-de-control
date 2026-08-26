#Una bodega espera sacos de 46 kg. Lee el peso e informa si cumple o debe revisarse por estar debajo del valor esperado.

weight= float(input("Ingrese el peso del saco en kg:"))

if weight < 46:
    print("El saco debe revisarse porque esta por debajo del peso esperado.")

else:
    print("El saco cumple con el peso establecido ")