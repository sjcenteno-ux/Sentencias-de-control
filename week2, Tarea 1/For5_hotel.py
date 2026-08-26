#Un restaurante recoge 10 calificaciones entre 1 y 5. Calcula el promedio y cuenta cuántas fueron 4 o 5.

total_rating=0
high_raing_count=0

for customer in range (1, 10):

    rating= int(input(f"Ingrese la calificacion (1-5) del cliente {customer}:"))

    total_rating= total_rating + rating

    if rating >= 4 and rating <= 5:
        high_raing_count= high_raing_count + 1
    else:
        print("Clasificacion invalida, solo se permiten del 1 al 5.")

average= total_rating / 10

print(f"El promedio de las calificaciones fue: {average}")
print(F"El totl de calificaciones mayores a  4 fueron: {high_raing_count}")