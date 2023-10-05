import datetime

def update_time_function(campo_minado):
        if campo_minado.started and not campo_minado.game_over and not campo_minado.is_game_over and not campo_minado.paused:
            elapsed_time = datetime.datetime.now() - campo_minado.start_time
            campo_minado.victory_time = elapsed_time
            elapsed_time_str = str(elapsed_time).split('.')[0]
            campo_minado.time_label.config(text=f"Tempo: {elapsed_time_str}")
            campo_minado.root.after(1000, campo_minado.update_time)