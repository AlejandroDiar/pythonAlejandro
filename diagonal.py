simbolo = "*"
altura = int(input("Introduce la altura: "))
for i in range(1, altura, 1):
    for j in range(i):
        print (" ", end="")
    print (simbolo)