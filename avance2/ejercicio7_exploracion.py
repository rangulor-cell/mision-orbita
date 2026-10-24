# Misión Órbita - Avance 2
# Ejercicio 7: Exploración científica
# Autor: Rachid Josué Angulo Rodríguez

# Entrada de recursos disponibles
energia = int(input("Ingrese la cantidad de energía disponible: "))
provisiones = int(input("Ingrese la cantidad de provisiones disponibles: "))

# Contadores y acumuladores
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0

# Variable de control del ciclo
exploracion_activa = True

# Ciclo principal de exploración
while exploracion_activa:
    print("\n--- MENÚ DE EXPLORACIÓN ---")
    print("Energía disponible:", energia)
    print("Provisiones disponibles:", provisiones)
    print("\n1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")

    opcion = int(input("Seleccione una opción: "))

    # Opción 1: analizar terreno
    if opcion == 1:
        if energia >= 8:
            energia = energia - 8
            puntos_cientificos = puntos_cientificos + 10
            actividades_realizadas = actividades_realizadas + 1

            print("\nAnálisis del terreno realizado correctamente.")
            print("Energía restante:", energia)
            print("Puntos científicos acumulados:", puntos_cientificos)
        else:
            print("\nNo hay energía suficiente para analizar el terreno.")
            print("La exploración ha finalizado.")
            exploracion_activa = False

    # Opción 2: recolectar muestra
    elif opcion == 2:
        if energia >= 12 and provisiones >= 2:
            energia = energia - 12
            provisiones = provisiones - 2
            puntos_cientificos = puntos_cientificos + 20
            actividades_realizadas = actividades_realizadas + 1
            muestras_recolectadas = muestras_recolectadas + 1

            print("\nMuestra recolectada correctamente.")
            print("Energía restante:", energia)
            print("Provisiones restantes:", provisiones)
            print("Puntos científicos acumulados:", puntos_cientificos)
            print("Muestras recolectadas:", muestras_recolectadas)
        else:
            print("\nNo hay recursos suficientes para recolectar la muestra.")

            if energia < 12:
                print("Energía insuficiente.")

            if provisiones < 2:
                print("Provisiones insuficientes.")

            print("La exploración ha finalizado.")
            exploracion_activa = False

    # Opción 3: realizar observación
    elif opcion == 3:
        if energia >= 5:
            energia = energia - 5
            puntos_cientificos = puntos_cientificos + 8
            actividades_realizadas = actividades_realizadas + 1

            print("\nObservación realizada correctamente.")
            print("Energía restante:", energia)
            print("Puntos científicos acumulados:", puntos_cientificos)
        else:
            print("\nNo hay energía suficiente para realizar la observación.")
            print("La exploración ha finalizado.")
            exploracion_activa = False

    # Opción 4: finalizar voluntariamente
    elif opcion == 4:
        print("\nExploración finalizada voluntariamente.")
        exploracion_activa = False

    # Opción incorrecta
    else:
        print("\nOpción no válida. Intente nuevamente.")

# Resumen final
print("\n========== RESUMEN DE EXPLORACIÓN ==========")
print("Actividades realizadas:", actividades_realizadas)
print("Muestras recolectadas:", muestras_recolectadas)
print("Puntos científicos obtenidos:", puntos_cientificos)
print("Energía restante:", energia)
print("Provisiones restantes:", provisiones)
print("============================================")