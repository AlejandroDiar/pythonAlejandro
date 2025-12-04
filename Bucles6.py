#Escribir un programa que pida al usuario un número entero y muestre por pantalla
#un triángulo rectángulo como el de más abajo, de altura el número introducido

altura = int(input("Introduce la altura del triangulo: "))

for x in range (1, altura + 1, 1):
    for i in range (2 * x - 1, 0, -2):
        if i > 1:
            print (i, end = " ")
        else:
            print (i)
