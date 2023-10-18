#!/usr/bin/python3
import tkinter as tk
import datetime
from functions.place_bombs import place_bombs_function
from functions.calculate_numbers import calculate_numbers_function
from functions.show_victory_popup import show_victory_popup_function
from functions.show_defeat_popup import show_defeat_popup_function
from functions.reveal_all_bombs import reveal_all_bombs_function
from functions.on_right_click import on_right_click_function
from functions.show_difficulty_menu import show_difficulty_menu_function
from functions.create_widgets import create_widgets_function
from functions.toggle_pause import toggle_pause_function
from functions.check_game_over import check_game_over_function
from functions.update_time import update_time_function
from functions.end_game import end_game_function


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
        self.revealed_cell_color = 'light gray'  # Cor de fundo para células reveladas
        self.is_game_over = False
        self.pause_button_enabled = True
        self.start_time = None
        self.pause_start_time = None
        self.flag_label = None
        self.bomb_label = None
        self.paused = False
        self.pause_button = None
        self.bomb_count = -2
        self.pause_label = None
        self.current_difficulty = ""
        self.victory_time = None
        self.create_widgets()
        self.place_bombs()
        calculate_numbers_function(self.field, self.rows, self.cols)

    def get_current_difficulty(self):
        return self.current_difficulty

    def create_widgets(self):
        create_widgets_function(self)

    def place_bombs(self):
        place_bombs_function(self.field, self.bombs)

    def abandon_game(self):
        if not self.game_over:
            show_difficulty_menu(self.root)

    def toggle_pause(self):
        toggle_pause_function(self)

    def update_time(self):
        update_time_function(self)

    def show_defeat_popup(self):
        show_defeat_popup_function(self.root, show_game)

    def show_victory_popup(self):
        show_victory_popup_function(self.victory_time, self.root, show_game)

    def check_game_over(self):
        check_game_over_function(self)

    def reveal_all_bombs(self):
        reveal_all_bombs_function(
            self.rows, self.cols, self.field, self.buttons)

    def end_game(self):
        end_game_function(self)

    def on_right_click(self, event, row, col):
        self.bomb_count = on_right_click_function(
            event, self.game_over, self.paused, self.bombs, self.flags, self.buttons, row, col, self.bomb_count, self.started)

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
            self.reveal_cell(row, col)
            self.flags[row][col] = True

        self.check_game_over()

    def reveal_cell(self, row, col):
        if (
            0 <= row < self.rows
            and 0 <= col < self.cols
            and not self.flags[row][col]
            and self.field[row][col] == 0
        ):
            self.flags[row][col] = True
            self.buttons[row][col].config(
                state=tk.DISABLED, bg=self.revealed_cell_color)

            for i in range(-1, 2):
                for j in range(-1, 2):
                    new_row = row + i
                    new_col = col + j
                    if (
                        0 <= new_row < self.rows
                        and 0 <= new_col < self.cols
                        and (new_row != row or new_col != col)
                    ):
                        self.reveal_cell(new_row, new_col)

        elif (
            0 <= row < self.rows
            and 0 <= col < self.cols
            and not self.flags[row][col]
            and self.field[row][col] != -1
        ):
            self.flags[row][col] = True
            bomb_count = self.field[row][col]
            self.buttons[row][col].config(
                text=str(bomb_count), bg=self.revealed_cell_color)

            if bomb_count == 0:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        new_row = row + i
                        new_col = col + j
                        if (
                            0 <= new_row < self.rows
                            and 0 <= new_col < self.cols
                        ):
                            self.reveal_cell(new_row, new_col)

    def show_intro_screen(self):
        intro_window = tk.Toplevel(self.root)
        intro_window.title("Introdução")

        num_bombs_label = tk.Label(
            intro_window, text=f"Número de Bombas: {self.bombs}")
        num_bombs_label.pack()

        num_flags_label = tk.Label(
            intro_window, text=f"Número de Bandeiras: {self.bombs + 2}")
        num_flags_label.pack()

        board_label = tk.Label(
            intro_window, text=f"Tabuleiro do Campo Minado: {self.rows} x {self.cols}")
        board_label.pack()

        intro_window.after(5000, intro_window.destroy)

        return True


def start_game(rows, cols, bombs, root, show_difficulty_menu):
    for widget in root.winfo_children():
        widget.destroy()

    game = CampoMinado(root, rows, cols, bombs, show_difficulty_menu)

    return game


def show_game(difficulty, show_difficulty_menu, root):
    game = None
    if difficulty == "Fácil":
        game = start_game(
            8, 8, 10, root, show_difficulty_menu_function(root, show_game))
        game.show_intro_screen()
        game.current_difficulty = "Fácil"
    elif difficulty == "Intermediário":
        game = start_game(10, 16, 30, root,
                          show_difficulty_menu_function(root, show_game))
        game.show_intro_screen()
        game.current_difficulty = "Intermediário"
    elif difficulty == "Difícil":
        game = start_game(24, 24, 100, root,
                          show_difficulty_menu_function(root, show_game))
        game.show_intro_screen()
        game.current_difficulty = "Difícil"

    return game


def show_difficulty_menu(root):
    show_difficulty_menu_function(root, show_game)


def main():
    root = tk.Tk()
    root.title("Campo Minado")

    show_difficulty_menu(root)

    root.mainloop()

# Instancia do jogo para testes


def create_game_instance(root, rows, cols, bombs):
    game = CampoMinado(root, rows, cols, bombs, lambda: None)
    return game


if __name__ == "__main__":
    main()
