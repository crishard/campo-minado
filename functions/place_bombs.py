import random

def place_bombs_function(field, bombs):
    bomb_count = 0
    while bomb_count < bombs:
        row = random.randint(0, len(field) - 1)
        col = random.randint(0, len(field[0]) - 1)
        if field[row][col] == 0:
            field[row][col] = -1
            bomb_count += 1
