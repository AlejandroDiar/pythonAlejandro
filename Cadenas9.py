#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
#dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
#anterior para que también funcione cuando el día o el mes se introduzcan con un
#solo carácter.
fechaN = input ("Introduce tu fecha de nacimiento en formato (dd/mm/aaaa): ")
dia = fechaN.split("/")[0]
mes = fechaN.split("/")[1]
anio = fechaN.split("/")[2]
print ("Naciste el dia " + dia + " del mes " + mes + " en el año " + anio + ".")