c = 1
ganadores = []
while c >= 1:
    print ("1. Salir")
    print ("2. Añadir numero ganador")
    opcion = input("Introduzca una opción: ")
    if opcion == "1":
        c = 0
        print ("Numeros ganadores:")
        ganadores.sort()
        for i in ganadores:
            print (i)
    elif opcion == "2":
        numero = input("Introduce el numero ganador: ")
        ganadores.append(numero)
    else:
        print ("Acción incorrecta.")

