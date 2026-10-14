# ============================================================
# Archivo: ejercicio4_lanzamiento.py
# Curso: SOFT-01 Principios de Programacion 1 - Seccion SCV6
# Integrante: Rachid Josue Angulo Rodriguez
# Fecha: 14/10/2026
# Version: 1.0
# Descripcion: Verifica las condiciones iniciales de lanzamiento.
# ============================================================

# Declaracion de constantes
RESERVA_COMBUSTIBLE = 10

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

oxigeno_disponible = int(
    input("Ingrese el oxigeno disponible: ")
)
oxigeno_requerido = int(
    input("Ingrese el oxigeno requerido: ")
)

energia_disponible = int(
    input("Ingrese la energia disponible: ")
)
energia_requerida = int(
    input("Ingrese la energia requerida: ")
)

provisiones_disponibles = int(
    input("Ingrese las provisiones disponibles: ")
)
provisiones_requeridas = int(
    input("Ingrese las provisiones requeridas: ")
)

# Procesamiento del combustible necesario para toda la mision
combustible_total = (
    combustible_ida
    + combustible_regreso
    + RESERVA_COMBUSTIBLE
)

# Salida del combustible total calculado
print()
print("Combustible total requerido:", combustible_total, "unidades")

# Decision doble con las cuatro condiciones de autorizacion
if (
    combustible_disponible >= combustible_total
    and oxigeno_disponible >= oxigeno_requerido
    and energia_disponible >= energia_requerida
    and provisiones_disponibles >= provisiones_requeridas
):
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La mision debe ser revisada")
