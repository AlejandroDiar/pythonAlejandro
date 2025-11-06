#En una determinada empresa, sus empleados son evaluados al final de cada año.
#Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir
#aumentando, traduciéndose en mejores beneficios. Los puntos que pueden
#conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores
#intermedios entre las cifras mencionadas. A continuación se muestra una tabla con
#los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida
#en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
#Escribir un programa que lea la puntuación del usuario e indique su nivel de
#rendimiento, así como la cantidad de dinero que recibirá el usuario.

dinero = float(input("Introduce la cantidad de dinero conseguida: "))
puntuacion = float (input("Introduzca su puntuación: "))
recibir = dinero * puntuacion
if puntuacion == 0.0:
    print ("Inaceptable, obtuviste " + str(recibir))
elif puntuacion == 0.4:
    print ("Aceptable, obtuviste " + str(recibir))
elif puntuacion == 0.6 or puntuacion == 0.8:
    print ("Meritorio, obtuviste " + str(recibir))
else:
    print ("Puntuación no válida.")
