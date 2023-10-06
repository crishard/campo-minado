import subprocess
import tkinter as tk
from campo_minado import create_game_instance, show_difficulty_menu, show_game, start_game, CampoMinado
from functions.show_difficulty_menu import show_difficulty_menu_function
import pytest

from functions.place_bombs import place_bombs_function



@pytest.fixture
def root():
    return tk.Tk()






def test_on_click_is_bomb(root):
    zone_row = 0
    zone_col = 0
    game = show_game("Fácil", show_difficulty_menu_function, root)

    for row in range(zone_row, zone_row + 3):
        for col in range(zone_col, zone_col + 3):
            game.field[row][col] = -1 

    game.on_button_click(zone_row, zone_col)

    # Verifique se o jogo termina (derrota) após o clique na zona
    assert game.game_over is True, "O jogo não terminou após o clique na zona com uma bomba."