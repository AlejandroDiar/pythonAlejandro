dinero = int(input("Introduce el dinero: "))
cinco = 0
dos = 0
uno = 0

while dinero > 0:
    while dinero >= 5:
        cinco = cinco + 1
        dinero = dinero - 5
    while dinero >= 2:
        dos = dos + 1
        dinero = dinero - 2
    while dinero >= 1:
        uno = uno + 1
        dinero = dinero - 1
print (cinco)
print (dos)
print (uno)  