def calculate_numbers_function(field, rows, cols):
        for row in range(rows):
            for col in range(cols):
                if field[row][col] == -1:
                    continue
                bomb_count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if 0 <= row + dr < rows and 0 <= col + dc < cols:
                            if field[row + dr][col + dc] == -1:
                                bomb_count += 1
                field[row][col] = bomb_count