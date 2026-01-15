frutas = {'Platano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruta = input("Elige una fruta: ")
kilos = float(input("Cuántos kilos? "))
precio = kilos * frutas[fruta]
print (kilos, " kg de " + str(fruta) + " son " ,round(precio,2), " €.")