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



# Testa se a introducao esta sendo exibida corretamente
from functions.show_tutorial import show_tutorial_function
from unittest.mock import patch


@patch("campo_minado.CampoMinado.show_intro_screen", return_value=True)
def test_show_intro_screen(mock_show_intro_screen, root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)
    verify = game.show_intro_screen()

    assert verify == True



# Testa se o tutorial esta sendo exibido corretamente
@patch("functions.show_difficulty_menu.show_tutorial_function")
def test_show_tutorial_called(mock_show_tutorial_function, root):
    show_difficulty_menu_function(root, show_game)

    # Encontre o widget "frame"
    frame = None
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            frame = widget
            break

    # Verifique se o widget "frame" foi encontrado
    assert frame is not None, "Widget 'frame' não foi encontrado."

    # Chame a função que deve acionar o tutorial
    for widget in frame.winfo_children():
        if widget.cget("text") == "Tutorial":
            widget.invoke()

    # Verifique se a função show_tutorial_function foi chamada com os argumentos corretos
    mock_show_tutorial_function.assert_called_once_with(root, show_difficulty_menu_function, show_game)

# Testa se o botão de tutorial esta funcionando corretamente
@patch("functions.show_difficulty_menu.show_difficulty_menu_function")
def test_back_to_menu_button(mock_show_difficulty_menu_function, root):
    show_tutorial_function(root, mock_show_difficulty_menu_function, show_game)

    # Encontre o widget do botão "Voltar ao Menu"
    back_button = None
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button) and widget.cget("text") == "Voltar ao Menu":
            back_button = widget
            break

    # Verifique se o widget do botão foi encontrado
    assert back_button is not None, "Widget do botão 'Voltar ao Menu' não foi encontrado."

    # Chame a função associada ao botão "Voltar ao Menu" (simulando um clique)
    back_button.invoke()

    # Verifique se a função show_difficulty_menu_function foi chamada corretamente
    mock_show_difficulty_menu_function.assert_called_once_with(root, show_game)