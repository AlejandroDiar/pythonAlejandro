#Escribir un programa que pida al usuario un número entero y muestre por pantalla si
#es par o impar

numero = int(input("Introduce un numero entero: "))
if numero != 0:
    if numero % 2 == 0:
        print ("El numero " + str(numero) + " es par.")
    else:
        print ("El numero " + str(numero) + " es impar.")
else: 
    print ("El numero 0 no es valido.")