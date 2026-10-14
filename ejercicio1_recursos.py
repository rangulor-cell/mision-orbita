# ============================================================
# Archivo: ejercicio1_recursos.py
# Curso: SOFT-01 Principios de Programacion 1 - Seccion SCV6
# Integrante: Rachid Josue Angulo Rodriguez
# Fecha: 14/10/2026
# Version: 1.0
# Descripcion: Calcula los recursos necesarios para una mision.
# ============================================================

# Declaracion de constantes
CONSUMO_COMBUSTIBLE_DIA = 8
RESERVA_COMBUSTIBLE = 10
CONSUMO_OXIGENO_DIA = 2
RESERVA_OXIGENO = 5
CONSUMO_ENERGIA_DIA = 5
ENERGIA_EXPLORACION = 10
CONSUMO_PROVISIONES_DIA = 1
RESERVA_PROVISIONES = 3

# Entrada de datos
nombre_mision = input("Ingrese el nombre de la mision:")
tripulantes = int(input("Ingrese la cantidad de tripulantes:"))
dias_viaje = int(input("Ingrese los dias estimados para llegar al destino: "))

# Procesamiento de los recursos necesarios para ida y regreso
combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
combustible_total = (
    combustible_ida
    + combustible_regreso
    + RESERVA_COMBUSTIBLE
)

oxigeno_requerido = (
    dias_viaje
    * CONSUMO_OXIGENO_DIA
    * 2
    * tripulantes
    + RESERVA_OXIGENO
)

energia_requerida = (
    dias_viaje
    * CONSUMO_ENERGIA_DIA
    * 2
    + ENERGIA_EXPLORACION
)

provisiones_requeridas = (
    dias_viaje
    * tripulantes
    * 2
    * CONSUMO_PROVISIONES_DIA
    + RESERVA_PROVISIONES
)

# Salida de resultados
print()
print("Resumen de recursos necesarios")
print("Mision:", nombre_mision)
print("Tripulantes:", tripulantes)
print("Duracion estimada hasta el destino:", dias_viaje, "dias")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Reserva de combustible:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Oxigeno requerido:", oxigeno_requerido, "unidades")
print("Energia requerida:", energia_requerida, "unidades")
print("Provisiones requeridas:", provisiones_requeridas, "unidades")