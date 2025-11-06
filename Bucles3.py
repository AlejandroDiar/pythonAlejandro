#Escribir un programa que pida al usuario un número entero positivo y muestre por
#pantalla todos los números impares desde 1 hasta ese número separados por
#comas.

n = int(input("Introduce un numero entero: "))
for x in range(1, n+1, 1):
    if x % 2 != 0:
        print (x)
