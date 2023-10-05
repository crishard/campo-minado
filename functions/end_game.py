def end_game_function(campo_minado):
        campo_minado.game_over = True
        campo_minado.time_label.config(text="Você perdeu!")
        campo_minado.reveal_all_bombs()
        campo_minado.pause_button_enabled = False
        campo_minado.show_defeat_popup()