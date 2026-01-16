diccionario = {}

p = 1
while p != 0:
    print ("1.Añadir opcion")
    print ("0.Salir")
    p = int(input("Elige opcion: "))
    if p == 1:
        dato = input("Añade un dato: ")
        valor = input("Añade valor al dato: ")
        diccionario.update({dato:valor})
        print(diccionario)
