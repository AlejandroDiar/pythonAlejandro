t = int(input("Que tabla desea: "))
m = int(input("Longitud de la tabla: "))

for i in range (1, m+1, 1):
    multiplicacion = t * i
    print (str(i)+" x "+str(t)+" = "+str(multiplicacion))
