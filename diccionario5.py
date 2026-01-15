creditosAsig = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
totalCreditos = 0

for asignatura, creditos in creditosAsig.items():
    totalCreditos = totalCreditos + creditos
    print (asignatura,"tiene",creditos,"créditos.")
print ("El total de créditos es de",totalCreditos,"créditos.")
