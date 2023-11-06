import pytest
import tkinter as tk

from campo_minado import  show_game
from functions.show_difficulty_menu import show_difficulty_menu_function

event = None
game_over = False
paused = False
bombs = 10
flags = [[False for _ in range(10)] for _ in range(10)]
buttons = [[tk.Button() for _ in range(10)] for _ in range(10)]
row = 5
col = 5
bomb_count = -2
started = True

def test_on_click_bomb():
    zone_row = 0
    zone_col = 0

    root = tk.Tk()

    game = show_game("Fácil", show_difficulty_menu_function, root)

    for row in range(zone_row, zone_row + 3):
        for col in range(zone_col, zone_col + 3):
            game.field[row][col] = -1 
    game.on_button_click(zone_row, zone_col)

    assert game.field[row][col] is -1 and game.game_over is True

def test_defeat_on_click_bomb():
    zone_row = 0
    zone_col = 0

    root = tk.Tk()

    game = show_game("Fácil", show_difficulty_menu_function, root)

    for row in range(zone_row, zone_row + 3):
        for col in range(zone_col, zone_col + 3):
            game.field[row][col] = -1 
    game.on_button_click(zone_row, zone_col)

    assert game.game_over is True



def test_on_click_bomb_medium_game():
    zone_row = 0
    zone_col = 0

    root = tk.Tk()

    game = show_game("Intermediário", show_difficulty_menu_function, root)

    for row in range(zone_row, zone_row + 3):
        for col in range(zone_col, zone_col + 3):
            game.field[row][col] = -1 
    game.on_button_click(zone_row, zone_col)

    assert game.field[row][col] is -1 and game.game_over is True

def test_defeat_on_click_bomb_medium_game():
    zone_row = 0
    zone_col = 0

    root = tk.Tk()

    game = show_game("Intermediário", show_difficulty_menu_function, root)

    for row in range(zone_row, zone_row + 3):
        for col in range(zone_col, zone_col + 3):
            game.field[row][col] = -1 
    game.on_button_click(zone_row, zone_col)

    assert game.game_over is True


def test_on_click_bomb_hard_game():
    zone_row = 0
    zone_col = 0

    root = tk.Tk()

    game = show_game("Difícil", show_difficulty_menu_function, root)

    for row in range(zone_row, zone_row + 3):
        for col in range(zone_col, zone_col + 3):
            game.field[row][col] = -1 
    game.on_button_click(zone_row, zone_col)

    assert game.field[row][col] is -1 and game.game_over is True

def test_defeat_on_click_bomb_hard_game():
    zone_row = 0
    zone_col = 0

    root = tk.Tk()

    game = show_game("Difícil", show_difficulty_menu_function, root)

    for row in range(zone_row, zone_row + 3):
        for col in range(zone_col, zone_col + 3):
            game.field[row][col] = -1 
    game.on_button_click(zone_row, zone_col)

    assert game.game_over is True
