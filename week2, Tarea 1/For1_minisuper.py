#Registra las ventas de lunes a domingo. Calcula el total semanal y el promedio diario.

weekly_total=0 
for day in range (1, 8):
    sale= float(input(f"Ingrese la cantidad vendida del dia {day}: C$"))

    weekly_total= weekly_total + sale      

    daily_average= weekly_total / 7

print(f"El total diario es de: C${daily_average:.2f}")
print(f"El total de la semana es de: C${weekly_total:.2f}")
