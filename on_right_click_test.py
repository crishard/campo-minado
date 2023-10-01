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

