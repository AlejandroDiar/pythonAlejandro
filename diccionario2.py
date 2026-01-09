nombre = input("Nombre: ")
edad = input("Edad: ")
direccion = input("Direccion: ")
telefono = input("Telefono: ")
diccionario = {'nombre':nombre, 'edad':edad, 'direccion':direccion, 'telefono':telefono}
print (f"{diccionario['nombre']} tiene {diccionario['edad']} años, vive en {diccionario['direccion']} y su numero de telefono es {diccionario['telefono']}")