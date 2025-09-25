def torre_hanoi(n, origen, auxiliar, destino):
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


# Ejemplo: resolver la torre de Hanoi con 3 discos
torre_hanoi(3, "A", "B", "C")
