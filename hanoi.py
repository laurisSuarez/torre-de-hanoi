def torre_hanoi(n, origen, auxiliar, destino):
    try:
        # Validar que n sea un número entero positivo
        if not isinstance(n, int) or n <= 0:
            raise ValueError("El número de discos debe ser un entero positivo.")

        # Caso base: si solo hay un disco, lo movemos directamente
        if n == 1:
            print(f"Mover disco 1 de {origen} a {destino}")
            return

        # Paso recursivo: mover n-1 discos a la torre auxiliar
        torre_hanoi(n-1, origen, destino, auxiliar)

        # Mover el disco más grande a la torre destino
        print(f"Mover disco {n} de {origen} a {destino}")

        # Mover los n-1 discos desde auxiliar hasta destino
        torre_hanoi(n-1, auxiliar, origen, destino)

    except RecursionError:
        print("Error: se ha alcanzado el límite máximo de recursión.")
    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


# Ejemplo correcto: resolver la torre de Hanoi con 3 discos
torre_hanoi(3, "A", "B", "C")

# Ejemplo con error: pasar un valor incorrecto
torre_hanoi(-2, "A", "B", "C")
