masa = float(input("Introduce tu peso en kg:"))
altura = float(input("Introduce tu altura en metros:"))
imc = masa / (altura ** 2)
print("Tu indice de masa corporal es: {:.2f}".format(imc))