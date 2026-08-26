# Un hospedaje de Granada ofrece una promoción simulada en temporada baja. 
# Dentro de esa temporada, el porcentaje depende de si la reserva alcanza 3 noches.

low_season= input ("¿La reserva es en temporada baja: si/no?")

if low_season.lower() == "si":
    nights= int(input("Ingrese la cantidad de noches: "))
    price= float(input("Ingrese el precio de la reserva: C$"))

    if nights >= 3:
     discount= price * 0.10
    else:
       discount= price * 0.5

    total= price - discount 
    print(f"El total a pagar es de: C${total:.2f}")

else:
   price= float(input("Ingrese el precio de la reserva: C$"))
   print(f"El total a pagar es: C${price:.2f}")

