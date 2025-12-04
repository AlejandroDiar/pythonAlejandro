asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
notas = []
for i in asignaturas:
    nota = int(input("Qué nota sacaste en "+i+"?"))
    notas.append(nota)
longitud = len(asignaturas)
for i in range (0, longitud, 1):
    print ("En "+asignaturas[i]+" has sacado un "+str(notas[i]))

