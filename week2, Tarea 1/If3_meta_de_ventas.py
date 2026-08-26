#Un emprendimiento fija una meta diaria de C$4,000. 
# Lee el total vendido e informa si se alcanzó; muestra cuánto faltó o cuánto se superó.

sales_total= float(input("Ingrese el total vendido del dia de hoy: C$"))
sales_goal= 4000
if sales_total < sales_goal:
    difference= sales_goal - sales_total
    print(f"Faltaron C${difference:.2f}, para alcanzar la meta diaria")

elif sales_total == sales_goal:
    print("Se alcanzo la meta diaria.")

else:
    difference= sales_total - sales_goal
    print(f"Se supero la meta diaria por C${difference:.2f}, felicidades.")

    