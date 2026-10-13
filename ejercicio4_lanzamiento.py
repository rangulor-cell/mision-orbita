# Proyecto: Mision Orbita
# Autor: Josue Angulo

combustible = float(input("Ingrese el combustible disponible: "))
oxigeno = float(input("Ingrese el oxigeno disponible: "))
energia = float(input("Ingrese la energia disponible: "))
provisiones = float(input("Ingrese las provisiones disponibles: "))

combustible_minimo = float(input("Ingrese el combustible minimo requerido: "))
oxigeno_minimo = float(input("Ingrese el oxigeno minimo requerido: "))
energia_minima = float(input("Ingrese la energia minima requerida: "))
provisiones_minimas = float(input("Ingrese las provisiones minimas requeridas: "))

if combustible >= combustible_minimo:
    if oxigeno >= oxigeno_minimo:
        if energia >= energia_minima:
            if provisiones >= provisiones_minimas:
                print("Lanzamiento autorizado")
            else:
                print("Lanzamiento NO autorizado")
        else:
            print("Lanzamiento NO autorizado")
    else:
        print("Lanzamiento NO autorizado")
else:
    print("Lanzamiento NO autorizado")