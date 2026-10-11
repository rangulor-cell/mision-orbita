# Proyecto: Mision Orbita
# Autor: Josue Angulo

combustible_disponible = float(input("Ingrese el combustible disponible: "))
combustible_necesario = float(input("Ingrese el combustible necesario: "))

if combustible_disponible >= combustible_necesario:
    print("La mision puede realizarse")
else:
    print("No hay suficiente combustible")