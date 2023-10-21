import tkinter as tk
from campo_minado import create_game_instance, show_difficulty_menu, show_game, start_game, CampoMinado
from functions.show_difficulty_menu import show_difficulty_menu_function
import pytest

from functions.place_bombs import place_bombs_function
from functions.on_right_click import on_right_click_function

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

@pytest.fixture
def root():
    return tk.Tk()

def test_end_game_bomb_click(root):
    zone_row = 1
    zone_col = 1
    board = [
        [0, -1, 0, 0],
        [0, 0, 0, -1],
        [-1, 0, -1, 0],
        [0, 0, 0, 0]
    ]

    game = create_game_instance(root, 4, 4, 4)
    game.field = board

    game.on_button_click(zone_row, zone_col)

    button_text = game.buttons[zone_row][zone_col]["text"]  # Número de bombas adjacentes
    assert game.game_over is True


def test_end_game_safe_zone_clicked(root):
    zone_row = 1
    zone_col = 2
    board = [
        [0, -1, 0, 0],
        [0, 0, 0, -1],
        [-1, 0, -1, 0],
        [0, 0, 0, 0]
    ]

    game = create_game_instance(root, 4, 4, 4)
    game.field = board

    game.on_button_click(zone_row, zone_col)
 # Número de bombas adjacentes
    assert game.is_game_over is False


def test_game_flag_zone_clicked():
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)

    assert game_over is False


def test_end_game_discovered_zone_clicked(root):
    zone_row = 1
    zone_col = 2
    board = [
        [0, -1, 0, 0],
        [0, 0, 0, -1],
        [-1, 0, -1, 0],
        [0, 0, 0, 0]
    ]

    game = create_game_instance(root, 4, 4, 4)
    game.field = board

    game.on_button_click(zone_row, zone_col)
    game.on_button_click(zone_row, zone_col)

    assert game.is_game_over is False



def test_all_zones_discoverd(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    # Define um valor padrão para células vazias (por exemplo, 0)
    default_value = [0]

    # Verifica se todas as células do tabuleiro têm valores diferentes do valor padrão
    for row in range(game.rows):
        for col in range(game.cols):
            cell_value = game.field[row][col]
            assert cell_value != default_value

    # Se todas as células tiverem valores diferentes do valor padrão, o teste é bem-sucedido
    assert True

def test_victory(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    # Define um valor padrão para células vazias (por exemplo, 0)
    default_value = [0]

    # Verifica se todas as células do tabuleiro têm valores diferentes do valor padrão
    for row in range(game.rows):
        for col in range(game.cols):
            cell_value = game.field[row][col]
            assert cell_value != default_value

    # Se todas as células tiverem valores diferentes do valor padrão, o teste é bem-sucedido
    assert game.victory_time != False

def test_last_safe_zone_clicked(root):
    board = [
        [0, -1, 0, 0],
        [0, 0, 0, -1],
        [-1, 0, -1, 0],
        [0, 0, 0, 0]
    ]

    game = create_game_instance(root, 4, 4, 4)
    game.field = board

    # Marca as outras zonas como descobertas
    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] == 0:
                game.buttons[row][col]["state"] = tk.DISABLED
                game.flags[row][col] = True
                game.buttons[row][col]["bg"] = game.revealed_cell_color

    # Verifique se a última zona segura que falta para ser descoberta não encerra o jogo
    zone_row = 3
    zone_col = 0
    game.on_button_click(zone_row, zone_col)

    assert game.is_game_over is False
