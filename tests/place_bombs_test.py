from campo_minado import show_game
from functions.place_bombs import place_bombs_function
from functions.show_difficulty_menu import show_difficulty_menu_function
import pytest
import tkinter as tk

@pytest.fixture
def root():
    return tk.Tk()

def teste_place_bombs_easy_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    assert game.bombs == 10 
def teste_place_bombs_medium_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)

    assert game.bombs == 30 
def teste_place_bombs_hard_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)

    assert game.bombs == 100 

def test_place_bombs_valid_counts():
    field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    bombs = 5
    place_bombs_function(field, bombs)
    bomb_count = sum(row.count(-1) for row in field)
    assert bomb_count == bombs

def test_place_bombs_valid_positions():
    field = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    bombs = 5
    place_bombs_function(field, bombs)
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == -1:
                assert 0 <= row < len(field) and 0 <= col < len(field[row])
                
def test_place_bombs_empty_field():
    field = []
    bombs = 0
    place_bombs_function(field, bombs)
    assert field == []


def test_place_bombs_all_bombs():
    field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    bombs = 9
    place_bombs_function(field, bombs)
    bomb_count = sum(row.count(-1) for row in field)
    assert bomb_count == 9


def test_place_bombs_no_bombs():
    field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    bombs = 0
    place_bombs_function(field, bombs)
    bomb_count = sum(row.count(-1) for row in field)
    assert bomb_count == 0


def test_place_bombs_bomb_count():
    field = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    bombs = 5
    place_bombs_function(field, bombs)
    bomb_count = sum(row.count(-1) for row in field)
    assert bomb_count == bombs


def test_place_bombs_no_extra_bombs():
    field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    bombs = 2
    place_bombs_function(field, bombs)
    bomb_count = sum(row.count(-1) for row in field)
    assert bomb_count == bombs

def test_place_bombs_negative_bombs():

    field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    bombs = -1
    place_bombs_function(field, bombs)
    bomb_count = sum(row.count(-1) for row in field)
    assert bomb_count == 0


def test_place_bombs_valid_range():
    field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    bombs = 5
    place_bombs_function(field, bombs)
    for row in field:
        for cell in row:
            if cell == -1:
                assert -1 <= cell <= 8

def test_place_bombs_invalid_field():
    field = None
    bombs = 5
    try:
        place_bombs_function(field, bombs)
    except Exception as e:
        assert str(e) == "Field cannot be None"

def test_place_bombs_invalid_bombs():
    field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    bombs = "5"
    try:
        place_bombs_function(field, bombs)
    except Exception as e:
        assert str(e) == "Bombs must be an integer"

def test_place_bombs_insufficient_space():
    field = [[-1, -1], [-1, -1]]
    bombs = 5
    try:
        place_bombs_function(field, bombs)
    except Exception as e:
        assert str(e) == "Not enough space for bombs"

def test_place_bombs_no_field():
    field = []
    bombs = 5
    try:
        place_bombs_function(field, bombs)
    except ValueError as e:
        assert str(e) == "Not enough space for bombs"
    assert field == []

def test_place_bombs_large_field():
    field = [[0] * 100 for _ in range(100)]
    bombs = 100
    place_bombs_function(field, bombs)
    bomb_count = sum(row.count(-1) for row in field)
    assert bomb_count == bombs

def test_place_bombs_large_bombs():
    field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    bombs = 100
    place_bombs_function(field, bombs)
    bomb_count = sum(row.count(-1) for row in field)
    assert bomb_count == 9

def test_place_bombs_max_bombs():
    field = [[0] * 100 for _ in range(100)]
    bombs = 10000
    place_bombs_function(field, bombs)
    bomb_count = sum(row.count(-1) for row in field)
    assert bomb_count == 10000

def test_place_bombs_random_bombs():
    field = [[0] * 10 for _ in range(10)]
    bombs = 5
    place_bombs_function(field, bombs)
    bomb_count = sum(row.count(-1) for row in field)
    assert bomb_count == bombs

def test_place_bombs_invalid_cell_value():
    field = [[0, 0, 'x'], [0, 0, 0], [0, 0, 0]]
    bombs = 5
    try:
        place_bombs_function(field, bombs)
    except Exception as e:
        assert str(e) == "Invalid cell value in the field"
