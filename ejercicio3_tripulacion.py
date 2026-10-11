# Proyecto: Mision Orbita
# Autor: Josue Angulo

oxigeno_disponible = float(input("Ingrese el oxigeno disponible: "))
oxigeno_necesario = float(input("Ingrese el oxigeno necesario: "))

provisiones_disponibles = float(input("Ingrese las provisiones disponibles: "))
provisiones_necesarias = float(input("Ingrese las provisiones necesarias: "))

if oxigeno_disponible >= oxigeno_necesario:
    if provisiones_disponibles >= provisiones_necesarias:
        print("La tripulacion cuenta con soporte suficiente")
    else:
        print("No hay suficientes provisiones")
else:
    print("No hay suficiente oxigeno")