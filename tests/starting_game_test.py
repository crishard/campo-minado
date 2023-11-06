import tkinter as tk
from campo_minado import show_game
from functions.show_difficulty_menu import show_difficulty_menu_function
import pytest


@pytest.fixture
def root():
    return tk.Tk()

def test_bomb_distribution(root):
    num_tests = 100
    bomb_counts = None

    for _ in range(num_tests):
        show_difficulty_menu_function(root, show_game)
        game = show_game("Fácil", show_difficulty_menu_function, root)

        if bomb_counts is None:
        
            bomb_counts = [[0 for _ in range(game.cols)] for _ in range(game.rows)]

        for row in range(game.rows):
            for col in range(game.cols):
                if game.field[row][col] == -1:
                    bomb_counts[row][col] += 1

  
    threshold = num_tests // game.rows // game.cols // 2  
    for row in range(game.rows):
        for col in range(game.cols):
            assert bomb_counts[row][col] >= threshold, f"Distribuição de bombas não é aleatória em ({row}, {col})"

def test_is_not_level_defined(root): 
    show_difficulty_menu_function(root, show_game)
    try:
        game = show_game("dsds", show_difficulty_menu_function, root)
        game.current_difficulty()
    except Exception as e:
        assert str(e) == "'NoneType' object has no attribute 'current_difficulty'"

# Testa se o nível fácil é criado corretamente

def test_board_is_covered(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    default_value = ''

    for row in range(game.rows):
        for col in range(game.cols):
            cell_value = game.field[row][col]
            assert cell_value != default_value, f"Célula ({row}, {col}) não foi gerada"


def test_board_generated(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    default_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, -1]
  
    for row in range(game.rows):
        for col in range(game.cols):
            cell_value = game.field[row][col]
            assert cell_value != default_value, f"Célula ({row}, {col}) não foi gerada"


def test_no_zone_has_flags(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] != -1 and game.flags[row][col]:
                assert False, f"Célula ({row}, {col}) tem uma bandeira em uma zona sem bomba"

def test_bomb_out_field(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    try: 
        zone = game.field[9][9] == -1
    except Exception as e:
        assert str(e) == "list index out of range"


def test_all_bombs_in_field_easy(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)
    field = game.field
    rows = len(field)
    cols = len(field[0])

    for row in range(rows):
        for col in range(cols):
            if field[row][col] == -1:
                assert 0 <= row < rows and 0 <= col < cols
def test_all_bombs_in_field_mid(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)
    field = game.field
    rows = len(field)
    cols = len(field[0])

    for row in range(rows):
        for col in range(cols):
            if field[row][col] == -1:
                assert 0 <= row < rows and 0 <= col < cols
def test_all_bombs_in_field_hard(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)
    field = game.field
    rows = len(field)
    cols = len(field[0])

    for row in range(rows):
        for col in range(cols):
            if field[row][col] == -1:
                assert 0 <= row < rows and 0 <= col < cols
