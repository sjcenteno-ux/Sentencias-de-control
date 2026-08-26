#Una cooperativa primero verifica si la humedad está entre 10% y 12%. 
# Si cumple, clasifica el lote según los defectos reportados. Propón categorías claras.

humidity = float(input("Ingrese el porcentaje de humedad del lote: "))

if humidity >= 10 and  humidity <= 12:
    defects = int(input("Ingrese la cantidad de defectos reportados: "))

    if defects <=2:
        print("El lote es de alta calidad ")
      

    elif defects <=6:
        print("El lote es de calidad media.")

    else:
        print("El lote es de calidad baja")

else:
    print("El lote no cumple con la humedad requerida ")

