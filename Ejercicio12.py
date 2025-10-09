#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene
#un descuento del 60%. Escribir un programa que comience leyendo el número de
#barras vendidas que no son del día. Después el programa debe mostrar el precio
#habitual de una barra de pan, el descuento que se le hace por no ser fresca y el
#coste final total.

b=int(input("Introduce el número de barras de pan que no son del dia: "))
bf= 3.49
bp= bf * 0.4
pp= bp * b
print ("El precio de cada barra de pan fresca es de " + str(round(bf, 2)) + " euros. El descuento que se le aplica a las barras de pan que ya no son del dia es del 60%, por lo que cada barra saldrá a " + str(round(bp, 2)) + " euros, siendo todas las barras un total de " + str(round(pp, 2)) + " euros.")