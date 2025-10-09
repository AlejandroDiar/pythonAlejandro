#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
#Suele hacer venta por correo y la empresa de logística les cobra por peso de cada
#paquete así que deben calcular el peso de los payasos y muñecas que saldrán en
#cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un
#programa que lea el número de payasos y muñecas vendidos en el último pedido y
#calcule el peso total del paquete que será enviado.

p=int(input("Introduce la cantidad de payasos a enviar: "))
m=int(input("Introduce la cantidad de muñecas a enviar: "))
pp= (p * 112) / 1000
pm= (m * 75) / 1000
pt = pp + pm

print ("Se han vendido un total de " + str(p) + " payasos y " + str(m) + " muñecas. El peso total del paquete es de " + str(pt) + " kg.")