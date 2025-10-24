#Escribir un programa que pida al usuario dos números y muestre por pantalla su
#división. Si el divisor es cero el programa debe mostrar un error.

n1 = float(input("Introduce el dividiendo: "))
n2 = float(input("Introduce el divisor: "))

if n2 == 0:
    print ("Error, el divisor no puede ser 0.")
else:
    c = float(n1 / n2)
    print ("El resultado es " + str(c) + ".")
