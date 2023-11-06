import tkinter as tk
from functions.show_tutorial import show_tutorial_function
from functions.show_history_function import display_history

def show_difficulty_menu_function(root, show_game):
    for widget in root.winfo_children():
        widget.destroy()

    frame = tk.Frame(root)
    frame.grid(row=0, column=0, padx=10, pady=10)

    label = tk.Label(frame, text="Escolha o nível de dificuldade:")
    label2 = tk.Label(frame, text="Mais ações dentro do jogo")
    label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    label2.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def show_history():
        display_history(root, show_difficulty_menu_function, show_game)

    def show_tutorial():
        show_tutorial_function(root, show_difficulty_menu_function, show_game)

    def close_game():
        root.destroy()

    def start_game_button(difficulty):
        show_game(difficulty, show_difficulty_menu_function, root)

    button_columns = {"Fácil": 0, "Intermediário": 1, "Difícil": 2}

    easy_button = tk.Button(frame, text="Fácil", command=lambda: start_game_button("Fácil"))
    intermediate_button = tk.Button(frame, text="Intermediário", command=lambda: start_game_button("Intermediário"))
    hard_button = tk.Button(frame, text="Difícil", command=lambda: start_game_button("Difícil"))

    easy_button.grid(row=1, column=button_columns["Fácil"], padx=10, pady=10)
    intermediate_button.grid(row=1, column=button_columns["Intermediário"], padx=10, pady=10)
    hard_button.grid(row=1, column=button_columns["Difícil"], padx=10, pady=10)

    history_button = tk.Button(frame, text='Histórico', command=show_history)
    history_button.grid(row=3, column=0, padx=10, pady=10)

    tutorial_button = tk.Button(frame, text='Tutorial', command=show_tutorial)
    tutorial_button.grid(row=3, column=1, padx=10, pady=10)

    close_game_button = tk.Button(frame, text='Sair do jogo', command=close_game)
    close_game_button.grid(row=3, column=2, padx=10, pady=10)
