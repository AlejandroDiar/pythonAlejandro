#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión.

d=float(input("¿Cuánto desea invertir?"))
p=float(input("¿Cuál es el interés anual en porcentaje?"))
a=float(input("¿Cuántos años vas a invertir?"))

i = (p / 100) + 1
c = (d * i) ** a
print ("El capital obtenido en " + str(a) + " años es de " + str(c))
