def reveal_all_bombs_function(rows, cols, field, buttons):
    for row in range(rows):
        for col in range(cols):
            if field[row][col] == -1:
                buttons[row][col].config(text='💣')