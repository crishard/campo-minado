import tkinter as tk
from campo_minado import create_game_instance, show_game
from functions.show_difficulty_menu import show_difficulty_menu_function
import pytest


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

    assert game.game_over is True


def test_on_click_has_adjacent_bombs(root):
    zone_row = 1
    zone_col = 1
    board = [
        [0, -1, 0, 0],
        [0, 0, 0, -1],
        [-1, 0, -1, 0],
        [0, 0, 0, 0]
    ]

    zone_row = 2
    zone_col = 2
    game = create_game_instance(root, 4, 4, 4)
    game.field = board

    game.on_button_click(zone_row, zone_col)

    button_text = game.buttons[zone_row][zone_col]["text"]
    expected_text = str(8)  # Número de bombas adjacentes
    assert button_text == "💣", f"A célula clicada não exibe o texto correto. Esperado: {expected_text}, Obtido: {button_text}"


def test_on_click_no_adjacent_bombs(root):
    
    board = [
        [0, -1, 0, 0],
        [0, 0, 0, -1],
        [-1, 0, -1, 0],
        [0, 0, 0, 0]
    ]

    zone_row = 1
    zone_col = 1
    game = create_game_instance(root, 4, 4, 4)
    game.field = board 

    
    game.on_button_click(zone_row, zone_col)

    button_text = game.buttons[zone_row][zone_col]["text"]
    expected_text = "0" 

    assert button_text == expected_text, f"A célula clicada não exibe o texto correto. Esperado: {expected_text}, Obtido: {button_text}"
