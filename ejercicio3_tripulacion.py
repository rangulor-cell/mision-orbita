# ============================================================
# Archivo: ejercicio3_tripulacion.py
# Curso: SOFT-01 Principios de Programacion 1 - Seccion SCV6
# Integrante: Rachid Josue Angulo Rodriguez
# Fecha: 14/10/2026
# Version: 1.0
# Descripcion: Verifica el soporte disponible para la tripulacion.
# ============================================================

# Entrada de datos
oxigeno_disponible = int(
    input("Ingrese el oxigeno disponible: ")
)
oxigeno_requerido = int(
    input("Ingrese el oxigeno requerido: ")
)
provisiones_disponibles = int(
    input("Ingrese las provisiones disponibles: ")
)
provisiones_requeridas = int(
    input("Ingrese las provisiones requeridas: ")
)

# Decision doble con una condicion compuesta
# Es necesario que los dos recursos sean suficientes.
if (
    oxigeno_disponible >= oxigeno_requerido
    and provisiones_disponibles >= provisiones_requeridas
):
    print("La nave posee recursos suficientes para la tripulacion.")
else:
    print("La nave no posee recursos suficientes para la tripulacion.")
