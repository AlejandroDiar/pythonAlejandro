saldo = float(0)
option = 0
while option != "4":
    print ("1. Reintegro")
    print ("2. Ingresar")
    print ("3. Saldo")
    print ("4. Salir")
    option = input("Que accion desea: ")
    if option == "1":
        dinero = float(input("Introduce la cantidad que desea sacar: "))
        if saldo - dinero >= 0:
            saldo = saldo - dinero
            print ("Has sacado "+str(dinero)+"€, te quedan "+str(saldo)+"€")
        else:
            print ("Insuficiente saldo")
    elif option == "2":
        dinero = float(input("Introduce la cantidad que desea ingresar: "))
        saldo = saldo + dinero
        print ("Has ingresado "+str(dinero)+"€, tienes "+str(saldo)+"€")
    elif option == "3":
        print ("Tienes "+str(saldo)+"€")
    elif option == "4":
        print("Saliendo... Has salido con éxito.")

        
