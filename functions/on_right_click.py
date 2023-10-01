def on_right_click_function(event, game_over, paused, bombs, flags, buttons, row, col, bomb_count):
    if game_over or paused:
        return bomb_count

        

    if not flags[row][col] and bomb_count < bombs:
        buttons[row][col].config(text='🏳')
        flags[row][col] = True
        bomb_count += 1
    elif buttons[row][col]['text'] == '🏳':
        buttons[row][col].config(text='')
        flags[row][col] = False
        bomb_count -= 1

    return bomb_count
