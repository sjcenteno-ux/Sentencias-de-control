#Leer la nota de un estudiante y decir si aprobo o su aprendizaje es inicial 
from colorama import Fore, Style
grade = int(input("Ingrese la nota del estudiante:"))

if grade >= 70:
    print(Fore.GREEN + "Usted a aprobado")
    
else :
    print(Fore.RED + "Su aprendizaje es inicial")
    print(Style.RESET_ALL)