# ============================================================
# Universidad: CENFOTEC
# Curso: Principios de Programación 1
# Proyecto: Misión Órbita - Avance 2
# Ejercicio 8: Regreso a la Tierra
# Estudiante: Rachid Josué Angulo Rodríguez
# Descripción:
# Programa que determina si la nave puede iniciar el regreso
# y evalúa los recursos disponibles para la tripulación.
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
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje_ida = int(
    input("Ingrese la cantidad de días del viaje de ida: ")
)
combustible = int(input("Ingrese el combustible disponible: "))
oxigeno = int(input("Ingrese el oxígeno disponible: "))
energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))

# Cálculo del combustible necesario para regresar
combustible_necesario_regreso = (
    dias_viaje_ida * CONSUMO_COMBUSTIBLE_DIA
)

print("\n========== EVALUACIÓN DEL REGRESO ==========")
print(
    "Combustible necesario para el regreso:",
    combustible_necesario_regreso
)
print("Combustible disponible:", combustible)

# Decisión principal
if combustible >= combustible_necesario_regreso:
    print("\nLa nave puede iniciar el regreso a la Tierra")
    print("Se ejecutará la simulación del caso A")
else:
    print("\nLa nave no tiene combustible suficiente")
    print("La tripulación quedó varada.")
    print("Se ejecutará el análisis del caso B")