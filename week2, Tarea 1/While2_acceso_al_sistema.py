#Solicita la clave hasta que sea correcta. Cuenta los intentos e informa cuántos fueron necesarios.

attemps=0

correct_passaword=  " UAMHOLA777 "

password= input("Ingrese la contreseña correcta: ")
attemps= attemps + 1

while password != correct_passaword:
    print("Clave incorrecta.")
    password= input("Ingrese la contraseña de nuevo:")
    attemps= attemps + 1

print("Clave correcta")
print(f"La cantidad de intentos fueron: {attemps}")