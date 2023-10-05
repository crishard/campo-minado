import datetime


def check_game_over_function(campo_minado):
        if all(campo_minado.field[row][col] == -1 or campo_minado.flags[row][col] for row in range(campo_minado.rows) for col in range(campo_minado.cols)):
            campo_minado.game_over = True
            campo_minado.victory_time = datetime.datetime.now() - campo_minado.start_time
            campo_minado.show_victory_popup()