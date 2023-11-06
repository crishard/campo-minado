def on_right_click_function(self, event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started):
    if not started:
        return bomb_count


    if game_over or paused:
        return bomb_count

    if not flags[row][col] and bomb_count < bombs:
        buttons[row][col].config(text='🏳')
        flags[row][col] = True
        bomb_count += 1
        self.used_flags += 1
    elif buttons[row][col]['text'] == '🏳':
        buttons[row][col].config(text='')
        flags[row][col] = False
        self.used_flags -= 1
        bomb_count -= 1

    self.update_flag_label()

    return bomb_count
