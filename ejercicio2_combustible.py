# Proyecto: Mision Orbita
# Autor: Josue Angulo

combustible_disponible = float(input("Ingrese el combustible disponible: "))
combustible_necesario = float(input("Ingrese el combustible necesario: "))

reserva_emergencia = combustible_necesario * 0.10

combustible_total = combustible_necesario + reserva_emergencia

print()
print("Combustible total requerido:", combustible_total)

if combustible_disponible >= combustible_total:
    print("La mision puede realizarse")
else:
    print("No hay suficiente combustible")