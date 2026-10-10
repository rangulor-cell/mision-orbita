# Proyecto: Mision Orbita
# Autor: Josue Angulo

tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias = int(input("Ingrese la cantidad de dias de la mision: "))

combustible = tripulantes * dias * 10
oxigeno = tripulantes * dias * 5
energia = tripulantes * dias * 8
provisiones = tripulantes * dias * 3

print()
print("Recursos necesarios para la mision")
print("Combustible:", combustible)
print("Oxigeno:", oxigeno)
print("Energia:", energia)
print("Provisiones:", provisiones)