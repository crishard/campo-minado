import datetime

def toggle_pause_function(campo_minado):
    if campo_minado.pause_button_enabled:
        if not campo_minado.game_over:
            campo_minado.paused = not campo_minado.paused
            if campo_minado.paused:
                campo_minado.pause_button.config(text='Retomar')
                campo_minado.pause_label.config(
                    text='Você precisa retomar o jogo para realizar alguma ação.')
                if campo_minado.started and campo_minado.start_time is not None:
                    campo_minado.pause_start_time = datetime.datetime.now()
            else:
                campo_minado.pause_button.config(text='Pausar')
                campo_minado.pause_label.config(text='')
                if campo_minado.started and campo_minado.pause_start_time is not None:
                    campo_minado.current_time = datetime.datetime.now()
                    campo_minado.start_time += campo_minado.current_time - campo_minado.pause_start_time
                    campo_minado.update_time()
    else:
        campo_minado.pause_label.config(text='O jogo acabou.')