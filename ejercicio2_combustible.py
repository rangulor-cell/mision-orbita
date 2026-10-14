# ============================================================
# Archivo: ejercicio2_combustible.py
# Curso: SOFT-01 Principios de Programacion 1 - Seccion SCV6
# Integrante: Rachid Josue Angulo Rodriguez
# Fecha: 14/10/2026
# Version: 1.0
# Descripcion: Verifica el margen adicional de combustible.
# ============================================================

# Declaracion de constantes
RESERVA_COMBUSTIBLE = 10
MARGEN_MINIMO = 10

# Entrada de datos
combustible_disponible = int(
    input("Ingrese el combustible disponible: ")
)
combustible_ida = int(
    input("Ingrese el combustible requerido para llegar: ")
)
combustible_regreso = int(
    input("Ingrese el combustible requerido para regresar: ")
)

# Procesamiento
combustible_total = (
    combustible_ida
    + combustible_regreso
    + RESERVA_COMBUSTIBLE
)

combustible_adicional = (
    combustible_disponible
    - combustible_total
)

# Salida obligatoria de resultados
print()
print("Verificacion de combustible")
print("Combustible disponible:", combustible_disponible, "unidades")
print("Combustible requerido para llegar:", combustible_ida, "unidades")
print("Combustible requerido para regresar:", combustible_regreso, "unidades")
print("Reserva de emergencia:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Combustible adicional:", combustible_adicional, "unidades")

# Decision simple: solamente muestra la advertencia si el margen es bajo
if combustible_adicional < MARGEN_MINIMO:
    print("Advertencia: el margen adicional de combustible es bajo.")