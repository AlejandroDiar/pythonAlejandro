#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de
#interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de
#año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que
#comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
#introducida por el usuario. Después el programa debe calcular y mostrar por pantalla
#la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada
#cantidad a dos decimales.

d=float(input("¿Cuánto desea invertir?"))
p=4

i = (p / 100) + 1
c1 = (d * i)
c2 = (c1 * i)
c3 = (c2 * i)
print ("Tras un año habremos pasado de " + str(round(d, 2)) + " a " + str(round(c1, 2)) + " euros, tras 2 años tendrás " + str(round(c2, 2)) + " euros, tras 3 años " + str(round(c3, 2)) + " euros.")