#Escribir un programa que pregunte el nombre el un producto, su precio y un número
#de unidades y muestre por pantalla una cadena con el nombre del producto seguido
#de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con
#tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

nombre = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio del producto: "))
cantidad = int(input("Introduce la cantidad de existencias del producto: "))
precioFinal = round(precio * cantidad, 2)

print ("Tenemos " + str(cantidad) + " " + str(nombre) + ", cada unidad tiene un valor de " + format(precio, '.2f') + " euros. El total de la suma de todas las unidades es " + format(precioFinal, '.2f') + " euros.")