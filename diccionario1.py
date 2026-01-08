diccionario = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input ("Introduce una divisa con su simbolo: ")

if divisa in diccionario:
    print ("El simbolo de la divisa es ", diccionario[divisa])