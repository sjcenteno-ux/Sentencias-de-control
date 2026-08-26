#Una pulpería vende al crédito solo a clientes registrados. 
#Si lo están, revisa que su saldo pendiente no supere C$500. Diseña los mensajes para todos los casos.

registered= input("El cliente que esta pidiendo el credito esta registrado. si/no:")

if registered.lower() == "si":
    balance= float(input("Ingrese el saldo pendiente del ciente: C$"))

    if balance <= 500:
        print("El cliente tiene credito disponible.")

    else:
        print("No puede realizar la compra porque su saldo pendiente supera los C$500")
else:
    print("El cliente no puede optar a credito porque no esta registrado.")