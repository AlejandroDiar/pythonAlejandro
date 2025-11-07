#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
#año que dura la inversión.

dinero = float(input("Introduce cantidad a invertir: "))
interes = float(input("Introduce el interes anual: "))
anios = int(input("Introduce cuantos años invertirás: "))

for x in range (1, anios+1, 1):
    dinero = dinero * ((interes/100)+1) 
print ("Año "+str(x)+" "+str(round(dinero, 2)) + "€")