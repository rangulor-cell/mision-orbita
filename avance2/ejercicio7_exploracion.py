# Universidad: CENFOTEC
# Curso: principios de Programación 1
# Proyecto: Misión Órbita - Avance 2
# Ejercicio 7: Exploración científica
# Estudiante: Rachid Josué Angulo Rodríguez
# Descripción:
# Programa que controla actividades de exploración científica,
# el consumo de recursos y la acumulación de puntos.

print("============================================")
print("       MISIÓN ÓRBITA - EXPLORACIÓN")
print("============================================")

# Entrada y validación de los recursos disponibles
recursos_validos = False

while recursos_validos == False:
    try:
        energia = int(
            input("Ingrese la cantidad de energía disponible: ")
        )

        provisiones = int(
            input("Ingrese la cantidad de provisiones disponibles: ")
        )

        if energia >= 0 and provisiones >= 0:
            recursos_validos = True
        else:
            print("\nLos recursos no pueden ser negativos.")
            print("Ingrese nuevamente la energía y las provisiones.\n")

    except ValueError:
        print("\nEntrada no válida.")
        print("La energía y las provisiones deben ser números enteros.\n")

# Contadores y acumuladores
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0

# Variable de control del ciclo
exploracion_activa = True

# Ciclo principal de exploración
while exploracion_activa == True:
    print("\n========== MENÚ DE EXPLORACIÓN ==========")
    print("Energía disponible:", energia)
    print("Provisiones disponibles:", provisiones)
    print("------------------------------------------")
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")
    print("==========================================")

    # Validación de la opción seleccionada
    try:
        opcion = int(input("Seleccione una opción del 1 al 4: "))

    except ValueError:
        print("\nEntrada no válida.")
        print("Debe ingresar un número del 1 al 4.")
        continue

    # Opción 1: analizar terreno
    if opcion == 1:
        if energia >= 8:
            energia = energia - 8
            puntos_cientificos = puntos_cientificos + 10
            actividades_realizadas = actividades_realizadas + 1

            print("\nAnálisis del terreno realizado correctamente.")
            print("Energía consumida: 8")
            print("Energía restante:", energia)
            print(
                "Puntos científicos acumulados:",
                puntos_cientificos
            )

        else:
            print("\nNo hay energía suficiente para analizar el terreno.")
            print("Se necesitan al menos 8 unidades de energía.")
            print("La exploración ha finalizado.")

            exploracion_activa = False

    # Opción 2: recolectar una muestra
    elif opcion == 2:
        if energia >= 12 and provisiones >= 2:
            energia = energia - 12
            provisiones = provisiones - 2
            puntos_cientificos = puntos_cientificos + 20
            actividades_realizadas = actividades_realizadas + 1
            muestras_recolectadas = muestras_recolectadas + 1

            print("\nMuestra recolectada correctamente.")
            print("Energía consumida: 12")
            print("Provisiones consumidas: 2")
            print("Energía restante:", energia)
            print("Provisiones restantes:", provisiones)
            print(
                "Puntos científicos acumulados:",
                puntos_cientificos
            )
            print(
                "Muestras recolectadas:",
                muestras_recolectadas
            )

        else:
            print(
                "\nNo hay recursos suficientes para recolectar "
                "la muestra."
            )

            if energia < 12:
                print("Energía insuficiente.")
                print("Se necesitan al menos 12 unidades de energía.")

            if provisiones < 2:
                print("Provisiones insuficientes.")
                print("Se necesitan al menos 2 provisiones.")

            print("La exploración ha finalizado.")

            exploracion_activa = False

    # Opción 3: realizar una observación
    elif opcion == 3:
        if energia >= 5:
            energia = energia - 5
            puntos_cientificos = puntos_cientificos + 8
            actividades_realizadas = actividades_realizadas + 1

            print("\nObservación realizada correctamente.")
            print("Energía consumida: 5")
            print("Energía restante:", energia)
            print(
                "Puntos científicos acumulados:",
                puntos_cientificos
            )

        else:
            print(
                "\nNo hay energía suficiente para realizar "
                "la observación."
            )
            print("Se necesitan al menos 5 unidades de energía.")
            print("La exploración ha finalizado.")

            exploracion_activa = False

    # Opción 4: finalizar voluntariamente
    elif opcion == 4:
        print("\nExploración finalizada voluntariamente.")

        exploracion_activa = False

    # Opción numérica incorrecta
    else:
        print("\nOpción no válida.")
        print("Debe seleccionar un número del 1 al 4.")

# Resumen final de la exploración
print("\n========== RESUMEN DE EXPLORACIÓN ==========")
print("Actividades realizadas:", actividades_realizadas)
print("Muestras recolectadas:", muestras_recolectadas)
print("Puntos científicos obtenidos:", puntos_cientificos)
print("Energía restante:", energia)
print("Provisiones restantes:", provisiones)
print("=============================================")
