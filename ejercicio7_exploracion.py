# ============================================================
# Universidad: CENFOTEC
# Curso: Principios de Programación 1
# Proyecto: Misión Órbita - Avance 2
# Ejercicio 7: Exploración científica
# Estudiante: Rachid Josué Angulo Rodríguez
# Descripción:
# Programa que controla las actividades de exploración
# científica, el consumo de recursos y la acumulación de puntos.
# ============================================================


# Constantes para analizar el terreno
ENERGIA_ANALIZAR_TERRENO = 8
PUNTOS_ANALIZAR_TERRENO = 10

# Constantes para recolectar una muestra
ENERGIA_RECOLECTAR_MUESTRA = 12
PROVISIONES_RECOLECTAR_MUESTRA = 2
PUNTOS_RECOLECTAR_MUESTRA = 20

# Constantes para realizar una observación
ENERGIA_REALIZAR_OBSERVACION = 5
PUNTOS_REALIZAR_OBSERVACION = 8

# Constantes para las opciones del menú
OPCION_ANALIZAR_TERRENO = 1
OPCION_RECOLECTAR_MUESTRA = 2
OPCION_REALIZAR_OBSERVACION = 3
OPCION_FINALIZAR_EXPLORACION = 4


# Título del programa
print("============================================")
print("       MISIÓN ÓRBITA - EXPLORACIÓN")
print("============================================")


# Entrada de los recursos disponibles
energia = int(
    input("Ingrese la cantidad de energía disponible: ")
)

provisiones = int(
    input("Ingrese la cantidad de provisiones disponibles: ")
)


# Inicialización de contadores y acumuladores
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0


# Variable de control del ciclo
exploracion_activa = True


# Ciclo principal de exploración
while exploracion_activa:

    print("\n========== MENÚ DE EXPLORACIÓN ==========")
    print("Energía disponible:", energia)
    print("Provisiones disponibles:", provisiones)
    print("------------------------------------------")
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")
    print("==========================================")

    opcion = int(
        input("Seleccione una actividad: ")
    )


    # Opción 1: analizar el terreno
    if opcion == OPCION_ANALIZAR_TERRENO:

        if energia >= ENERGIA_ANALIZAR_TERRENO:

            energia = (
                energia - ENERGIA_ANALIZAR_TERRENO
            )

            puntos_cientificos = (
                puntos_cientificos
                + PUNTOS_ANALIZAR_TERRENO
            )

            actividades_realizadas = (
                actividades_realizadas + 1
            )

            print(
                "Actividad realizada: Analizar terreno. "
                "Puntos obtenidos: 10"
            )

        else:

            print(
                "Recursos insuficientes para realizar la actividad. "
                "La exploración finaliza."
            )

            exploracion_activa = False


    # Opción 2: recolectar una muestra
    elif opcion == OPCION_RECOLECTAR_MUESTRA:

        if (
            energia >= ENERGIA_RECOLECTAR_MUESTRA
            and provisiones >= PROVISIONES_RECOLECTAR_MUESTRA
        ):

            energia = (
                energia - ENERGIA_RECOLECTAR_MUESTRA
            )

            provisiones = (
                provisiones - PROVISIONES_RECOLECTAR_MUESTRA
            )

            puntos_cientificos = (
                puntos_cientificos
                + PUNTOS_RECOLECTAR_MUESTRA
            )

            actividades_realizadas = (
                actividades_realizadas + 1
            )

            muestras_recolectadas = (
                muestras_recolectadas + 1
            )

            print(
                "Actividad realizada: Recolectar muestra. "
                "Puntos obtenidos: 20"
            )

        else:

            print(
                "Recursos insuficientes para realizar la actividad. "
                "La exploración finaliza."
            )

            exploracion_activa = False


    # Opción 3: realizar una observación
    elif opcion == OPCION_REALIZAR_OBSERVACION:

        if energia >= ENERGIA_REALIZAR_OBSERVACION:

            energia = (
                energia - ENERGIA_REALIZAR_OBSERVACION
            )

            puntos_cientificos = (
                puntos_cientificos
                + PUNTOS_REALIZAR_OBSERVACION
            )

            actividades_realizadas = (
                actividades_realizadas + 1
            )

            print(
                "Actividad realizada: Realizar observación. "
                "Puntos obtenidos: 8"
            )

        else:

            print(
                "Recursos insuficientes para realizar la actividad. "
                "La exploración finaliza."
            )

            exploracion_activa = False


    # Opción 4: finalizar la exploración
    elif opcion == OPCION_FINALIZAR_EXPLORACION:

        print(
            "Exploración finalizada por la tripulación."
        )

        exploracion_activa = False


    # Opción numérica incorrecta
    else:

        print("Opción no válida.")


# Resumen final de la exploración
print("\n========== RESUMEN DE EXPLORACIÓN ==========")

print(
    "Actividades realizadas:",
    actividades_realizadas
)

print(
    "Muestras recolectadas:",
    muestras_recolectadas
)

print(
    "Puntos científicos:",
    puntos_cientificos
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

print("=============================================")