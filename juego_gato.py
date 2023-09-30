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

def obtener_entrada(jugador):
    while True:
        try:
            entrada = int(input(f"Jugador {jugador}, elige una posición (1-9): "))
            if 1 <= entrada <= 9:
                return entrada
            else:
                print("La entrada debe estar entre 1 y 9. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada no válida. Inténtalo de nuevo.")

def juego_gato():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugadores = ["X", "O"]
    turno = 0
    jugadas = 0

    while True:
        jugador_actual = jugadores[turno % 2]

        imprimir_tablero(tablero)
        entrada = obtener_entrada(jugador_actual)

        fila = (entrada - 1) // 3
        columna = (entrada - 1) % 3

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

        turno += 1

if __name__ == "__main__":
    juego_gato()

