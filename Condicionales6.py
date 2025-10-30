#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y
#el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y
#los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un
#programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
#que le corresponde.

#nombre = input("Introduce tu nombre: ")

gen = input ("Introduce tu genero (M/F): ")
name = input ("Introduce tu nombre: ")
nombre = name.upper()
genero = gen.upper()
Amujeres = "M"
Ahombres = "N"
if genero == "F" and nombre < Amujeres:
    print (str(nombre) + " pertenece al grupo A.")
elif genero == "F" and nombre > Amujeres:
    print (str(nombre) + " pertenece al grupo B.")
elif genero == "M" and nombre > Ahombres:
    print (str(nombre) + " pertenece al grupo A.")
elif genero == "M" and nombre < Ahombres:
    print (str(nombre) + " pertenece al grupo B.")
