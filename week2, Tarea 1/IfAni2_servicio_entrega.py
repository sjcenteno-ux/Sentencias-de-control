#Un emprendimiento calcula una tarifa simulada según zona urbana o rural y, dentro de cada zona.
#según si el paquete supera 5 kg. Propón tarifas y calcula el total.
zone= input("Ingrese a que zona pertenece: urbana/rural:")
weight= float(input("Ingrese el peso en kg de su paquete: "))

if zone.lower() == "urbana":
    if weight > 5:
        shipping_cost= 80
    else:
         shipping_cost= 50

else:
    if weight > 5:
        shipping_cost= 120
    else:
        shipping_cost= 80

print(f"El costo del envio es de: C${shipping_cost}")