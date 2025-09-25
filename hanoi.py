# Torres de Hanoi con recursividad
# Cumple con numeración de pasos y total de movimientos

paso = 0  # variable global para contar pasos

def hanoi(n, torre1, torre2, torre3): #define variables 
    global paso
    if n == 1:
        paso += 1
        print(f"Paso {paso}: mover disco desde {torre1} hacia {torre3}")
        return
    
    # mover n-1 discos de torre1 a torre2
    hanoi(n - 1, torre1, torre3, torre2)
    
    # mover el disco más grande
    paso += 1
    print(f"Paso {paso}: mover disco desde {torre1} hacia {torre3}")
    
    # mover n-1 discos de torre2 a torre3
    hanoi(n - 1, torre2, torre1, torre3)


# Bloque principal
try:
    cantidad = int(input("¿Cuántos discos quieres mover? (1-20): "))
    if cantidad < 1 or cantidad > 20:
        print("El número de discos debe estar entre 1 y 20.")
    else:
        hanoi(cantidad, "A", "B", "C")
        total = 2**cantidad - 1 # num movimientosm por num de discos formula
        print(f"\nTotal de movimientos: {paso} (esperado: {total})")
except ValueError:
    print("Error: Ingresa un número entero válido.")
