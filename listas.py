lista = ["lunes","martes","miercoles"] #listas creacion.
print (lista[0])                       # imprimimos primera posicion de la lista.
lista.append("jueves")                 # añadir objeto a la lista.
lista[0]="viernes"                     # sustituir elemento de una posicion por otro.
print (lista)                          # imprimir valores de la lista.

lista1 = ["Manzana","Pera"]
lista2 = ["Mango","Platano"]
lista3 = lista1 + lista2
print (lista1)                         #con esto podemos juntar filas.
print (lista2)
print (lista3)
lista3.pop(2)                          #con pop sacamos valores de la lista, es como eliminarlos.
print (lista3)
lista2.insert(1,"naranja")             #añadimos naranja en posicion 1, el que estabaantes en posicion 1
print (lista2)                         #el elemento que estaba antes en posicion 1 pasará a la 2.


#a = [[1,2],[3,4]]

#for i in range(len(a)):
#    for j in range