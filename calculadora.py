# ===== 1. Cabecera =====
# Programa: calcula el precio final de una compra aplicando descuentos
#   - 10 % si la compra es de 100 euros o más
#   - 15 % si la compra es de 300 euros o más
# Autores: Diego Sánchez Azorín y [compañero/a]
# Fecha: 01/10/2026

# ===== 2. Declaración de bibliotecas =====
# No hace falta ninguna biblioteca

# ===== 3. Declaración de funciones =====
# Devuelve el descuento que toca según el importe
def calcular_descuento(importe):
    if importe >= 300:
        return 0.15
    elif importe >= 100:
        return 0.10
    else:
        return 0.0

def main():
    # ===== 4. Declaración de variables =====
    importe = 0.0      # lo que cuesta la compra sin descuento
    descuento = 0.0    # porcentaje de descuento (0, 0.10 o 0.15)
    total = 0.0        # lo que paga el cliente al final

    # ===== 5. Entrada =====
    try:
        importe = float(input("Introduce el importe de la compra: "))
    except ValueError:
        print("Error: tienes que escribir un número.")
        return

    # ===== 6. Control =====
    if importe < 0:
        print("Error: el importe no puede ser negativo.")
    else:
        descuento = calcular_descuento(importe)
        total = importe - importe * descuento

        # ===== 7. Salida =====
        print(f"Descuento aplicado: {descuento * 100:.0f} %")
        print(f"Total a pagar: {total:.2f} euros")

    input("\nPulsa Enter para salir...")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()