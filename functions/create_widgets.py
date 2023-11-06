import tkinter as tk
def create_widgets_function(campo_minado):    
    campo_minado.frame = tk.Frame(campo_minado.root)
    campo_minado.frame.grid(row=1, column=1, padx=10, pady=10)

    campo_minado.pause_label = tk.Label(campo_minado.frame, text='')
    campo_minado.pause_label.grid(
        row=campo_minado.rows + 3, columnspan=campo_minado.cols + 1, pady=5)
    button_frame = tk.Frame(campo_minado.frame)
    button_frame.grid(row=campo_minado.rows + 2, columnspan=campo_minado.cols + 1, pady=5)

    campo_minado.pause_button = tk.Button(
        button_frame, text='Pausar', command=campo_minado.toggle_pause)
    campo_minado.pause_button.pack(side=tk.LEFT, padx=10)

    campo_minado.abandon_button = tk.Button(
        button_frame, text='Abandonar', command=campo_minado.abandon_game)
    campo_minado.abandon_button.pack(side=tk.LEFT, padx=10)

    restart_button = tk.Button(
        button_frame, text='Reiniciar', command=campo_minado.restart_game)
    restart_button.pack(side=tk.LEFT, padx=10)
    
    campo_minado.flag_label = tk.Label(campo_minado.frame, text="Bandeiras para uso: {campo_minado.bombs}")
    campo_minado.flag_label.grid(row=campo_minado.rows + 4, columnspan=campo_minado.cols + 1, pady=5)
    campo_minado.update_flag_label()


    for row in range(campo_minado.rows):
        letter_label = tk.Label(campo_minado.frame, text=chr(65 + row))
        letter_label.grid(row=row + 1, column=0, padx=3)

    for col in range(campo_minado.cols):
        number_label = tk.Label(campo_minado.frame, text=str(col + 1), pady=2)
        number_label.grid(row=0, column=col + 1)

    for row in range(campo_minado.rows):
        for col in range(campo_minado.cols):
            button = tk.Button(campo_minado.frame, text='', command=lambda r=row,
                                c=col: campo_minado.on_button_click(r, c), width=2, bg='white')
            button.grid(row=row + 1, column=col + 1)
            campo_minado.buttons[row][col] = button
            button.bind("<Button-3>", lambda event, r=row,
                        c=col: campo_minado.on_right_click(event, r, c))

    campo_minado.time_label = tk.Label(campo_minado.frame, text="Tempo: 0")
    campo_minado.time_label.grid(
        row=campo_minado.rows + 1, columnspan=campo_minado.cols + 1, pady=8)
