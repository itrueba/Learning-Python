# Solucionador de Sudoku con Backtracking

Este script en Python implementa un solucionador de Sudoku utilizando la técnica de backtracking.

## Cómo Utilizar

1. Ejecuta el script.
2. Define tu tablero de Sudoku como una lista de listas, donde cada lista interna representa una fila del Sudoku.
3. Utiliza el número `-1` para indicar las celdas vacías en el tablero.
4. Llama a la función `solve_sudoku` con tu tablero como argumento.
5. La función modificará el tablero y devolverá `True` si se encuentra una solución o `False` si el Sudoku es irresoluble.

## Uso

```python
if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
