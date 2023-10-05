import subprocess
import tkinter as tk
from campo_minado import create_game_instance, show_difficulty_menu, show_game, start_game, CampoMinado
from functions.show_difficulty_menu import show_difficulty_menu_function
import pytest



@pytest.fixture
def root():
    return tk.Tk()

# Testa se o nível fácil é criado corretamente


def test_start_game_easy(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)
    current_difficulty = game.get_current_difficulty()
    assert current_difficulty == "Fácil"

# Testa se o nível intermediário é selecionado corretamente


def test_start_game_intermediate(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)
    current_difficulty = game.get_current_difficulty()
    assert current_difficulty == "Intermediário"

# Testa se o nível difícil é selecionado corretamente


def test_start_game_hard(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)
    current_difficulty = game.get_current_difficulty()
    assert current_difficulty == "Difícil"


# Simula a criação da janela de escolha de nível
def test_choose_difficulty_window(root):
    show_difficulty_menu(root)

    assert len(root.winfo_children()) > 0
    assert isinstance(root.winfo_children()[0], tk.Frame)
    frame = root.winfo_children()[0]

    buttons = frame.winfo_children()

    assert any(button.winfo_class() == 'Button' for button in buttons)

#  Testa se as dimenssoes estao corretas
def test_dimension_easy(root): 
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    assert game.rows and game.cols == 8

def test_dimension_mid(root): 
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)

    assert game.rows == 10 and game.cols == 16


def test_dimension_hard(root): 
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)

    assert game.rows and game.cols == 24

# verifica se o tabuleiro inciou coberto
def test_matriz_easy(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    for row in range(game.rows):
        for col in range(game.cols):
            button = game.buttons[row][col]
            assert isinstance(button, tk.Button)


def test_matriz_mid(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)

    for row in range(game.rows):
        for col in range(game.cols):
            button = game.buttons[row][col]
            assert isinstance(button, tk.Button)
def test_matriz_hard(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)

    for row in range(game.rows):
        for col in range(game.cols):
            button = game.buttons[row][col]
            assert isinstance(button, tk.Button)

# teste de jogada no tabuleiro
def test_play_in_matriz_easy(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    row_to_click = 0
    col_to_click = 0

    game_instance = game
    click = game_instance.on_button_click(row_to_click, col_to_click)

    assert click is not False

def test_play_outside_matrix_easy(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    row_to_click = game.rows + 1  
    col_to_click = game.cols + 1  

    game_instance = game

    try:
        click = game_instance.on_button_click(row_to_click, col_to_click)
    except Exception as e:
        assert str(e) == "list index out of range" 


def test_play_in_matriz_mid(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)

    row_to_click = 0
    col_to_click = 0


    game_instance = game
    click = game_instance.on_button_click(row_to_click, col_to_click)

    assert click is not False

# testa jogada fora da matriz
def test_play_outside_matrix_mid(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    row_to_click = game.rows + 1
    col_to_click = game.cols + 1

    game_instance = game

    try:
        click = game_instance.on_button_click(row_to_click, col_to_click)
    except Exception as e:
        assert str(e) == "list index out of range" 

def test_play_in_matriz_hard(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)

    row_to_click = 0
    col_to_click = 0 

    game_instance = game
    click = game_instance.on_button_click(row_to_click, col_to_click)

    assert click is not False

def test_play_outside_matrix_hard(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)

    row_to_click = game.rows + 1  
    col_to_click = game.cols + 1 

    game_instance = game

    try:
        click = game_instance.on_button_click(row_to_click, col_to_click)
    except Exception as e:
        assert str(e) == "list index out of range" 

# testa se o tabuleiro nao e vazio
def test_non_empty_board_easy(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)


    rows = game.rows
    cols = game.cols

    assert rows > 0 and cols > 0, "O tabuleiro é de tamanho vazio"

    assert True


def test_non_empty_board_mid(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)


    rows = game.rows
    cols = game.cols

    assert rows > 0 and cols > 0, "O tabuleiro é de tamanho vazio"

    assert True


def test_non_empty_board_hard(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)


    rows = game.rows
    cols = game.cols

    assert rows > 0 and cols > 0, "O tabuleiro é de tamanho vazio"

    assert True
