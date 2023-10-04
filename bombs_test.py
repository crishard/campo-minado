import subprocess
import tkinter as tk
from campo_minado import create_game_instance, show_difficulty_menu, show_game, start_game, CampoMinado
from functions.show_difficulty_menu import show_difficulty_menu_function
import pytest



@pytest.fixture
def root():
    return tk.Tk()

# Testa se o nível fácil é criado corretamente

def test_bombs_game_easy_is_bigger(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    bombs_test = 12

    assert bombs_test > game.bombs

def test_bombs_game_easy_is_smaller(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    bombs_test = 5

    assert bombs_test < game.bombs
