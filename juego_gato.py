def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

def verificar_victoria(tablero, jugador):
    # Verificar filas y columnas
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)):
            return True
        if all(tablero[j][i] == jugador for j in range(3)):
            return True
    
    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or \
       all(tablero[i][2 - i] == jugador for i in range(3)):
        return True
    
    return False

def juego_gato():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"
    jugadas = 0

    while True:
        imprimir_tablero(tablero)
        fila = int(input(f"Jugador {jugador_actual}, elige una fila (0, 1, 2): "))
        columna = int(input(f"Jugador {jugador_actual}, elige una columna (0, 1, 2): "))

        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador_actual
            jugadas += 1
        else:
            print("Esa casilla ya está ocupada. Inténtalo de nuevo.")
            continue

        if verificar_victoria(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡Jugador {jugador_actual} ha ganado!")
            break
        elif jugadas == 9:
            imprimir_tablero(tablero)
            print("¡Empate!")
            break

        jugador_actual = "O" if jugador_actual == "X" else "X"

if __name__ == "__main__":
    juego_gato()

