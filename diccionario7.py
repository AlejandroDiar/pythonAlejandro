diccionario = {}
respuesta = 0
total = 0
while respuesta != "si":
    articulo = input("¿Qué artículo quieres añadir? ")
    precio = float(input("Introduce el precio del articulo: "))
    diccionario[articulo] = precio
    total = total + precio
    respuesta = input("¿Quieres terminar la lista?" )
print ("Lista de la compra:")
for articulo, precio in diccionario.items():
    print (articulo, " = ", precio, "€")
print ("TOTAL DE LA CESTA = ", total, "€")