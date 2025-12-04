total=float(0)
m = float(0)
for i in range(1,10,1):
    n=float(input("Introduce un numero: "))
    if n > m:
        m = n
    total = total + n
print ("El numero mayor es "+str(m))
print ("La suma de los numeros es "+str(total))
