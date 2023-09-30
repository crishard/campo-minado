# No arquivo functions/place_bombs.py

import random

def place_bombs_function(field, bombs):
    if field is None:
        raise ValueError("Field cannot be None")
    
    bombs = int(bombs)
    
    empty_cells = sum(row.count(0) for row in field)
    
    # Verificar se há espaço suficiente para as bombas
    if bombs > empty_cells:
        bombs = empty_cells  # Coloque apenas o número de bombas que cabe no campo
    
    bomb_count = 0
    while bomb_count < bombs:
        row = random.randint(0, len(field) - 1)
        col = random.randint(0, len(field[0]) - 1)
        if field[row][col] == 0:
            field[row][col] = -1
            bomb_count += 1
