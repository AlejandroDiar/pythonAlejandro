#Escribir un programa que pida al usuario que introduzca una frase en la consola y
#una vocal, y después muestre por pantalla la misma frase pero con la vocal
#introducida en mayúscula.

f = input("Introduce una frase: ")
v = input("Introduce una vocal: ")
f = f.replace(v, v.upper())
print(f)