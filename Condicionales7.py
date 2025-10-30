#Los tramos impositivos para la declaración de la renta en un determinado país son
#los siguientes:
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla
#el tipo impositivo que le corresponde.
renta = float(input("Introduce tu renta anual: "))
if renta < 10000:
    print ("Con " + str(renta) + " euros de renta te corresponde un tipo impositivo del 5%")
elif renta >= 10000 and renta < 20000:
     print ("Con " + str(renta) + " euros de renta te corresponde un tipo impositivo del 15%")
elif renta >= 20000 and renta < 35000:
          print ("Con " + str(renta) + " euros de renta te corresponde un tipo impositivo del 20%")
elif renta >= 35000 and renta < 60000:
           print ("Con " + str(renta) + " euros de renta te corresponde un tipo impositivo del 30%")
elif renta >= 60000:
             print ("Con " + str(renta) + " euros de renta te corresponde un tipo impositivo del 45%")
