asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
aprobadas = []
notas = []

for i in asignaturas:
    nota = int(input("Qué nota sacaste en "+i+"?"))
    notas.append(nota)
    if nota >= 5:
        aprobadas.append(i)

for i in aprobadas:
    asignaturas.remove(i)
longitud = len(asignaturas)
if longitud < 1:
    print ("Has aprobado todas.")
else:
    print ("Asignaturas a repetir:")
    for i in asignaturas:
        print (i)

 