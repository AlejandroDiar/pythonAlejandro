#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
#Los ingredientes para cada tipo de pizza aparecen a continuación.
#● Ingredientes vegetarianos: Pimiento y tofu.
#● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y
#en función de su respuesta le muestre un menú con los ingredientes disponibles
#para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
#tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la
#pizza elegida es vegetariana o no y todos los ingredientes que lleva.

print ("Bienvenido a la pizzería Bella Napoli!!!")
pizza = input("Pizza vegetariana o no [v/n]: ")
pizzaMayus = pizza.upper()
if pizzaMayus == "V":
    ingredientes = input("Que desea añadir a su pizza vegetariana? Pimiento o Tofu?")
    ingredientesMin = ingredientes.lower()
    print ("Tu pizza vegetariana lleva mozzarella, tomate y " + str(ingredientesMin) + ".")
elif pizzaMayus == "N":
    ingredientes = input("Que desea añadir a su pizza? Peperoni, jamon o salmon?")
    ingredientesMin = ingredientes.lower()
    print ("Tu pizza lleva mozzarella, tomate y " + str(ingredientesMin) + ".")

