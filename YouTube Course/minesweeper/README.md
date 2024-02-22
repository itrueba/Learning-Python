# Juego de Buscaminas

Este script en Python implementa el clásico juego de Buscaminas. El jugador debe excavar casillas sin bombas y evitar hacer clic en una casilla con una bomba.

## Cómo Jugar

1. Ejecuta el script.
2. El tablero se mostrará con celdas ocultas.
3. Ingresa la ubicación donde te gustaría excavar en formato `row, col` cuando se te indique.
4. Si la celda no contiene una bomba, se revelará el número de bombas circundantes o estarás libre de bombas.
5. Si la celda contiene una bomba, el juego termina.
6. Repite los pasos 2-5 hasta descubrir todas las celdas seguras o hacer clic en una bomba.

## Uso

```bash
python main.py