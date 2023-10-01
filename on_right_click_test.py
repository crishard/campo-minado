import pytest
from functions.on_right_click import on_right_click_function
import tkinter as tk

event = None
game_over = False
paused = False
bombs = 10
flags = [[False for _ in range(10)] for _ in range(10)]
buttons = [[tk.Button() for _ in range(10)] for _ in range(10)]
row = 5
col = 5
bomb_count = -2

# Testa se a função retorna o valor de bomb_count quando o jogo está encerrado


def test_on_right_click_function_game_over():
    result = on_right_click_function(
        event, True, paused, bombs, flags, buttons, row, col, bomb_count)
    assert result == bomb_count

# Testa se a função retorna o valor de bomb_count quando o jogo está pausado


def test_on_right_click_function_paused():
    result = on_right_click_function(
        event, game_over, True, bombs, flags, buttons, row, col, bomb_count)
    assert result == bomb_count

# Testa se a função incrementa bomb_count e configura a bandeira quando ela não está definida


def test_on_right_click_function_flag_not_set():
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count)
    assert result == bomb_count + 1
    assert flags[row][col] is True
    assert buttons[row][col]['text'] == '🏳'


# Testa se a função decrementa bomb_count e remove a bandeira quando ela já está definida

def test_on_right_click_function_flag_set():
    flags[row][col] = True
    buttons[row][col]['text'] = '🏳'
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count)
    assert result == bomb_count - 1
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''
