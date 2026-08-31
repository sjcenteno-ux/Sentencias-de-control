#Una motocicleta inicia con 8 litros. 
# Registra el consumo de cada recorrido mientras quede combustible y alerta al llegar a 1 litro.


fuel = 8

while fuel > 1:
    consumption = float(input("Ingrese el consumo del recorrido en litros: "))

    if consumption <= fuel:
        fuel = fuel - consumption
        print(f"Combustible restante: {fuel:.2f} litros.")
    else:
        print("El consumo ingresado supera el combustible disponible.")

print("ALERTA: El combustible llegó a 1 litro o menos.")