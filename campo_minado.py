import tkinter as tk
import random
import datetime
from functions.place_bombs import place_bombs_function
from functions.calculate_numbers import calculate_numbers_function
from functions.show_victory_popup import show_victory_popup_function
from functions.show_defeat_popup import show_defeat_popup_function
from functions.reveal_all_bombs import reveal_all_bombs_function
from functions.on_right_click import on_right_click_function


class CampoMinado:
    def __init__(self, root, rows, cols, bombs, show_difficulty_menu):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.field = [[0 for _ in range(cols)] for _ in range(rows)]
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.flags = [[False for _ in range(cols)] for _ in range(rows)]
        self.started = False
        self.show_difficulty_menu = show_difficulty_menu
        self.game_over = False
        self.is_game_over = False
        self.pause_button_enabled = True
        self.start_time = None
        self.pause_start_time = None
        self.paused = False
        self.pause_button = None
        self.bomb_count = -2
        self.pause_label = None
        self.victory_time = None
        self.create_widgets()
        self.place_bombs()
        calculate_numbers_function(self.field, self.rows, self.cols)

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=1, column=1, padx=10, pady=10)

        self.pause_label = tk.Label(self.frame, text='')
        self.pause_label.grid(
            row=self.rows + 3, columnspan=self.cols + 1, pady=5)
        button_frame = tk.Frame(self.frame)
        button_frame.grid(row=self.rows + 2, columnspan=self.cols + 1, pady=5)

        self.pause_button = tk.Button(
            button_frame, text='Pausar', command=self.toggle_pause)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.abandon_button = tk.Button(
            button_frame, text='Abandonar', command=self.abandon_game)
        self.abandon_button.pack(side=tk.LEFT, padx=10)

        for row in range(self.rows):
            letter_label = tk.Label(self.frame, text=chr(65 + row))
            letter_label.grid(row=row + 1, column=0, padx=3)

        for col in range(self.cols):
            number_label = tk.Label(self.frame, text=str(col + 1), pady=2)
            number_label.grid(row=0, column=col + 1)

        for row in range(self.rows):
            for col in range(self.cols):
                button = tk.Button(self.frame, text='', command=lambda r=row,
                                   c=col: self.on_button_click(r, c), width=2)
                button.grid(row=row + 1, column=col + 1)
                self.buttons[row][col] = button
                button.bind("<Button-3>", lambda event, r=row,
                            c=col: self.on_right_click(event, r, c))

        self.time_label = tk.Label(self.frame, text="Tempo: 0")
        self.time_label.grid(
            row=self.rows + 1, columnspan=self.cols + 1, pady=8)

    def place_bombs(self):
        place_bombs_function(self.field, self.bombs)

    def abandon_game(self):
        if not self.game_over:
            self.show_difficulty_menu()

    def toggle_pause(self):
        if self.pause_button_enabled:

            if not self.game_over:
                self.paused = not self.paused
                if self.paused:
                    self.pause_button.config(text='Retomar')
                    self.pause_label.config(
                        text='Você precisa retomar o jogo para realizar alguma ação.')
                    self.pause_start_time = datetime.datetime.now()
                else:
                    self.pause_button.config(text='Pausar')
                    self.pause_label.config(text='')
                    if self.started:
                        self.current_time = datetime.datetime.now()
                        self.start_time += self.current_time - self.pause_start_time
                        self.update_time()
        else:
            self.pause_label.config(text='O jogo acabou.')

    def update_time(self):
        if self.started and not self.game_over and not self.is_game_over and not self.paused:
            elapsed_time = datetime.datetime.now() - self.start_time
            self.victory_time = elapsed_time
            elapsed_time_str = str(elapsed_time).split('.')[0]
            self.time_label.config(text=f"Tempo: {elapsed_time_str}")
            self.root.after(1000, self.update_time)

    def show_defeat_popup(self):
        show_defeat_popup_function(self.root, self.show_difficulty_menu)

    def show_victory_popup(self):
        show_victory_popup_function(self.victory_time, self.root, self.show_difficulty_menu)

    def check_game_over(self):
        if all(self.field[row][col] == -1 or self.flags[row][col] for row in range(self.rows) for col in range(self.cols)):
            self.game_over = True
            self.victory_time = datetime.datetime.now() - self.start_time
            self.show_victory_popup()

    def reveal_all_bombs(self):
       reveal_all_bombs_function(self.rows, self.cols, self.field, self.buttons)

    def end_game(self):
        self.game_over = True
        self.time_label.config(text="Você perdeu!")
        self.reveal_all_bombs()
        self.pause_button_enabled = False
        self.show_defeat_popup()

    def on_right_click(self, event, row, col):
        self.bomb_count = on_right_click_function(event, self.game_over, self.paused, self.bombs, self.flags, self.buttons, row, col, self.bomb_count)

    def on_button_click(self, row, col):
        if self.game_over or self.is_game_over or self.flags[row][col] or self.paused:
            return

        if not self.started:
            self.started = True
            self.start_time = datetime.datetime.now()
            self.update_time()

        if self.is_game_over or self.flags[row][col]:
            return

        if self.field[row][col] == -1:
            self.end_game()
        else:
            bomb_count = self.field[row][col]
            self.buttons[row][col].config(text=str(bomb_count))
            self.flags[row][col] = True

        self.check_game_over()


def start_game(rows, cols, bombs, root, show_difficulty_menu):
    for widget in root.winfo_children():
        widget.destroy()

    game = CampoMinado(root, rows, cols, bombs, show_difficulty_menu)


def main():
    root = tk.Tk()
    root.title("Campo Minado")

    def show_difficulty_menu():
        for widget in root.winfo_children():
            widget.destroy()

        frame = tk.Frame(root)
        frame.grid(row=0, column=0, padx=10, pady=10)

        label = tk.Label(frame, text="Escolha o nível de dificuldade:")
        label2 = tk.Label(frame, text="Mais acoes dentro do jogo")
        label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        label2.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        def show_history():
            # Implementar a lógica para exibir o histórico
            pass

        def show_tutorial():
            tutorial_text = """
            Tutorial do Campo Minado:

            Regras do Jogo:

            1. O objetivo do jogo é abrir todos os campos sem bombas.
            2. Cada campo aberto mostrará um número, indicando quantas bombas estão adjacentes a ele.
            3. Use a lógica para determinar onde as bombas estão e evite clicar nelas.
            4. Use botões direito para marcar campos suspeitos com bandeiras.
            5. Marque todas as bombas para vencer o jogo.

            Boa sorte e divirta-se jogando!
            """
            for widget in root.winfo_children():
                widget.destroy()

            tutorial_label = tk.Label(
                root, text=tutorial_text, font=("Helvetica", 14), justify="left", padx=20, pady=20)
            tutorial_label.pack()

            back_button = tk.Button(
                root, text="Voltar ao Menu", command=show_difficulty_menu, pady=10)
            back_button.pack(side=tk.BOTTOM, pady=10)

        def close_game():
            root.destroy()

        def start_game_button(difficulty):
            show_game(difficulty, show_difficulty_menu)

        easy_button = tk.Button(frame, text="Fácil",
                                command=lambda: start_game_button("Fácil"))
        intermediate_button = tk.Button(
            frame, text="Intermediário", command=lambda: start_game_button("Intermediário"))
        hard_button = tk.Button(frame, text="Difícil",
                                command=lambda: start_game_button("Difícil"))

        easy_button.grid(row=1, column=0, padx=10, pady=10)
        intermediate_button.grid(row=1, column=1, padx=10, pady=10)
        hard_button.grid(row=1, column=2, padx=10, pady=10)
        history_button = tk.Button(
            frame, text='Histórico', command=show_history)
        history_button.grid(row=3, column=0, padx=10, pady=10)

        tutorial_button = tk.Button(
            frame, text='Tutorial', command=show_tutorial)
        tutorial_button.grid(row=3, column=1, padx=10, pady=10)

        close_game_button = tk.Button(
            frame, text='Sair do jogo', command=close_game)
        close_game_button.grid(row=3, column=2, padx=10, pady=10)

    def show_game(difficulty, show_difficulty_menu):
        if difficulty == "Fácil":
            start_game(8, 8, 1, root, show_difficulty_menu)
        elif difficulty == "Intermediário":
            start_game(10, 16, 30, root, show_difficulty_menu)
        elif difficulty == "Difícil":
            start_game(24, 24, 100, root, show_difficulty_menu)

    show_difficulty_menu()

    root.mainloop()


if __name__ == "__main__":
    main()
