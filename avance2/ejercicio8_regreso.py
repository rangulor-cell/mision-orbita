# ============================================================
# Universidad: CENFOTEC
# Curso: Principios de Programación 1
# Proyecto: Misión Órbita - Avance 2
# Ejercicio 8: Regreso a la Tierra
# Estudiante: Rachid Josué Angulo Rodríguez
# Descripción:
# Programa que determina si la nave puede iniciar el regreso,
# simula el viaje día por día y calcula la supervivencia de
# la tripulación cuando no puede regresar.
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

# Cálculo de los consumos diarios según la tripulación
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

        # Verificación de los recursos necesarios para el día
        if (
            combustible >= CONSUMO_COMBUSTIBLE_DIA
            and oxigeno >= oxigeno_necesario_dia
            and energia >= CONSUMO_ENERGIA_DIA
            and provisiones >= provisiones_necesarias_dia
        ):
            # Consumo de recursos
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

            # Actualización de contadores
            dias_completados = dias_completados + 1

            # Estado diario de la nave
            print(
                "Día",
                dia_actual,
                "| Combustible:",
                combustible,
                "| Oxígeno:",
                oxigeno,
                "| Energía:",
                energia,
                "| Provisiones:",
                provisiones
            )

            dia_actual = dia_actual + 1

        else:
            print(
                "\nEl regreso se interrumpió en el día",
                dia_actual
            )

            # Identificación de recursos insuficientes
            if combustible < CONSUMO_COMBUSTIBLE_DIA:
                print("Recurso insuficiente: combustible")

            if oxigeno < oxigeno_necesario_dia:
                print("Recurso insuficiente: oxígeno")

            if energia < CONSUMO_ENERGIA_DIA:
                print("Recurso insuficiente: energía")

            if provisiones < provisiones_necesarias_dia:
                print("Recurso insuficiente: provisiones")

            print("La tripulación no completó el regreso.")

            regreso_activo = False

    # Resultado del regreso
    if dias_completados == dias_viaje_ida:
        print(
            "\nLa tripulación regresó exitosamente "
            "a la Tierra."
        )
        print(
            "Combustible restante:",
            combustible,
            "unidades"
        )
        print(
            "Oxígeno restante:",
            oxigeno,
            "unidades"
        )
        print(
            "Energía restante:",
            energia,
            "unidades"
        )
        print(
            "Provisiones restantes:",
            provisiones,
            "unidades"
        )

# Caso B: combustible insuficiente para iniciar el regreso
else:
    print("\nLa nave no tiene combustible suficiente.")
    print("La tripulación quedó varada en el destino.")

    # Cálculo de días de supervivencia por recurso
    dias_oxigeno = (
        oxigeno // oxigeno_necesario_dia
    )

    dias_energia = (
        energia // CONSUMO_ENERGIA_DIA
    )

    dias_provisiones = (
        provisiones // provisiones_necesarias_dia
    )

    # Determinar los días de supervivencia sin utilizar min()
    dias_supervivencia = dias_oxigeno

    if dias_energia < dias_supervivencia:
        dias_supervivencia = dias_energia

    if dias_provisiones < dias_supervivencia:
        dias_supervivencia = dias_provisiones

    # Mostrar cálculos de supervivencia
    print("\n========== ANÁLISIS DE SUPERVIVENCIA ==========")
    print("Días posibles con oxígeno:", dias_oxigeno)
    print("Días posibles con energía:", dias_energia)
    print(
        "Días posibles con provisiones:",
        dias_provisiones
    )
    print(
        "La tripulación puede sobrevivir",
        dias_supervivencia,
        "días."
    )

    print("Recurso o recursos limitantes:")

    # Mostrar todos los recursos limitantes
    if dias_oxigeno == dias_supervivencia:
        print("Oxígeno")

    if dias_energia == dias_supervivencia:
        print("Energía")

    if dias_provisiones == dias_supervivencia:
        print("Provisiones")

    print("================================================")