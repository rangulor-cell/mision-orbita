# ============================================================
# Universidad: CENFOTEC
# Curso: Principios de Programación 1
# Proyecto: Misión Órbita - Avance 2
# Ejercicio 8: Regreso a la Tierra
# Estudiante: Rachid Josué Angulo Rodríguez
# Descripción:
# Programa que determina si la nave puede iniciar el regreso,
# simula el viaje día por día y evalúa los recursos.
# ============================================================

# Constantes de consumo diario
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_TRIPULANTE_DIA = 1

print("============================================")
print("       MISIÓN ÓRBITA - REGRESO")
print("============================================")

# Entrada de datos
tripulantes = int(
    input("Ingrese la cantidad de tripulantes: ")
)

dias_viaje_ida = int(
    input("Ingrese la cantidad de días del viaje de ida: ")
)

combustible = int(
    input("Ingrese el combustible disponible: ")
)

oxigeno = int(
    input("Ingrese el oxígeno disponible: ")
)

energia = int(
    input("Ingrese la energía disponible: ")
)

provisiones = int(
    input("Ingrese las provisiones disponibles: ")
)

# Cálculo del combustible necesario para regresar
combustible_necesario_regreso = (
    dias_viaje_ida * CONSUMO_COMBUSTIBLE_DIA
)

# Cálculo del consumo diario según la tripulación
oxigeno_necesario_dia = (
    tripulantes * CONSUMO_OXIGENO_TRIPULANTE_DIA
)

provisiones_necesarias_dia = (
    tripulantes * CONSUMO_PROVISIONES_TRIPULANTE_DIA
)

print("\n========== EVALUACIÓN DEL REGRESO ==========")
print(
    "Combustible necesario para el regreso:",
    combustible_necesario_regreso
)
print("Combustible disponible:", combustible)

# Caso A: combustible suficiente para iniciar el regreso
if combustible >= combustible_necesario_regreso:
    print("\nLa nave puede iniciar el regreso a la Tierra.")
    print(
        "La duración del regreso será de",
        dias_viaje_ida,
        "días."
    )

    # Variables para controlar el ciclo
    dia_actual = 1
    dias_completados = 0
    regreso_activo = True

    # Simulación del regreso día por día
    while dia_actual <= dias_viaje_ida and regreso_activo == True:
        print(
            "\n================ DÍA",
            dia_actual,
            "================"
        )

        print("Recursos antes del consumo:")
        print("Combustible:", combustible)
        print("Oxígeno:", oxigeno)
        print("Energía:", energia)
        print("Provisiones:", provisiones)

        # Verificar si hay recursos para completar el día
        if (
            combustible >= CONSUMO_COMBUSTIBLE_DIA
            and oxigeno >= oxigeno_necesario_dia
            and energia >= CONSUMO_ENERGIA_DIA
            and provisiones >= provisiones_necesarias_dia
        ):
            # Consumir los recursos correspondientes al día
            combustible = (
                combustible - CONSUMO_COMBUSTIBLE_DIA
            )

            oxigeno = (
                oxigeno - oxigeno_necesario_dia
            )

            energia = (
                energia - CONSUMO_ENERGIA_DIA
            )

            provisiones = (
                provisiones - provisiones_necesarias_dia
            )

            # Actualizar los contadores
            dias_completados = dias_completados + 1

            print(
                "\nDía",
                dia_actual,
                "completado correctamente."
            )

            print("Recursos restantes:")
            print("Combustible:", combustible)
            print("Oxígeno:", oxigeno)
            print("Energía:", energia)
            print("Provisiones:", provisiones)

            dia_actual = dia_actual + 1

        else:
            print("\nEl regreso no puede continuar.")

            # Identificación de los recursos insuficientes
            if combustible < CONSUMO_COMBUSTIBLE_DIA:
                print("Motivo: combustible insuficiente.")

            if oxigeno < oxigeno_necesario_dia:
                print("Motivo: oxígeno insuficiente.")

            if energia < CONSUMO_ENERGIA_DIA:
                print("Motivo: energía insuficiente.")

            if provisiones < provisiones_necesarias_dia:
                print("Motivo: provisiones insuficientes.")

            regreso_activo = False

    # Resultado del regreso
    print("\n========== RESULTADO DEL REGRESO ==========")

    if dias_completados == dias_viaje_ida:
        print("Regreso exitoso.")
        print("La tripulación llegó a la Tierra.")
    else:
        print("Regreso interrumpido.")
        print("La tripulación no logró llegar a la Tierra.")

    print("Días requeridos:", dias_viaje_ida)
    print("Días completados:", dias_completados)
    print("Combustible restante:", combustible)
    print("Oxígeno restante:", oxigeno)
    print("Energía restante:", energia)
    print("Provisiones restantes:", provisiones)
    print("===========================================")

# Caso B: combustible insuficiente para iniciar el regreso
else:
    print("\nLa nave no tiene combustible suficiente.")
    print("La tripulación quedó varada.")
    print("El análisis de supervivencia se agregará después.")