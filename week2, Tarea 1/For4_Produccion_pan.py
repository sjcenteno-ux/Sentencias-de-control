#Una panadería registra durante 6 días la producción y las ventas. Calcula totales y producto sobrante.

total_production= 0
total_sales=0 

for day in range (1, 7):
   production= int(input(f"Ingrese cuantos panes se hornearon el dia {day}:"))
   sales= int(input(f"Ingrese cuantos panes se vendieron el dia {day}:"))
   total_production = total_production + production 
   total_sales = total_sales + sales

lefover= total_production - total_sales

print(f"La venta total del pan fue: {total_sales}")
print(F"El sobrante de los panes fue: {lefover}")