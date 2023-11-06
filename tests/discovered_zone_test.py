import pytest
import tkinter as tk
from campo_minado import show_game
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



#  Testa se existe alguma bandeira na zona
def test_no_flag_before_button_click():
    cell_row = 0
    cell_col = 0
    
    assert flags[cell_row][cell_col] is False, f"A célula ({cell_row}, {cell_col}) possui uma bandeira antes do clique."

#  Testa se a zona esta descoberta antes do click
def test_zone_already_discovered_before_button_click():
    zone_row = 0
    zone_col = 0

    buttons = [[{'text': '1'} for _ in range(8)] for _ in range(8)]  
  
    for row in range(zone_row, zone_row + 3):
        for col in range(zone_col, zone_col + 3):
            assert buttons[row][col]['text'] != '', f"A célula ({row}, {col}) não está descoberta antes do clique."

#  Testa se a zona esta coberta antes do click
def test_zone_is_covered_before_button_click():
    zone_row = 0
    zone_col = 0

    buttons = [[{'text': ''} for _ in range(8)] for _ in range(8)]

    for row in range(zone_row, zone_row + 3):
        for col in range(zone_col, zone_col + 3):
            assert buttons[row][col]['text'] == '', f"A célula ({row}, {col}) não está coberta antes do clique."

#  Testa se a zona contem bomba- jogador deve perder a partida
def test_zone_contains_bomb():
    zone_row = 0
    zone_col = 0

    root = tk.Tk()

    game = show_game("Fácil", show_difficulty_menu_function, root)

    for row in range(zone_row, zone_row + 3):
        for col in range(zone_col, zone_col + 3):
            game.field[row][col] = -1 

    game.on_button_click(zone_row, zone_col)

    assert game.game_over is True, "O jogo não terminou após o clique na zona com uma bomba."

#  Testa se a zona esta descoberta apos o click
def test_zone_discoverd_after_click():
    zone_row = 0
    zone_col = 0

    root = tk.Tk()

    game = show_game("Fácil", show_difficulty_menu_function, root)

    for row in range(zone_row, zone_row + 3):
        for col in range(zone_col, zone_col + 3):
            game.field[row][col] = ''  

    game.on_button_click(zone_row, zone_col)

    assert game.buttons[row][col] != '', "O jogo não terminou após o clique na zona com uma bomba."

