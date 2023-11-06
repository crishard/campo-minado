import tkinter as tk
from campo_minado import show_game, start_game
from functions.show_difficulty_menu import show_difficulty_menu_function
import pytest



@pytest.fixture
def root():
    return tk.Tk()

# Testa se o nível fácil é criado corretamente

def test_bombs_game_easy_is_bigger(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    assert game.bombs == 10

def test_bombs_game_easy_is_smaller(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    bombs_test = 5

    assert bombs_test < game.bombs

def test_bombs_game_easy_is_corret(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    bombs_test = 10

    assert bombs_test == game.bombs


def test_board_contains_only_bombs_easy(root):
    show_difficulty_menu_function(root, show_game)
    game = start_game(8, 8, 64, root, show_difficulty_menu_function(root, show_game))

    
    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] != -1:  
                assert False, f"Célula ({row}, {col}) não contém uma bomba"

    assert True


def test_bombs_game_mid_is_bigger(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)

    bombs_test = 32

    assert bombs_test > game.bombs

def test_bombs_game_mid_is_smaller(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)

    bombs_test = 20

    assert bombs_test < game.bombs

def test_bombs_game_mid_is_correct(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)

    bombs_test = 30

    assert bombs_test == game.bombs


def test_board_contains_only_bombs_mid(root):
    show_difficulty_menu_function(root, show_game)
    game = start_game(10, 16, 160, root, show_difficulty_menu_function(root, show_game))

    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] != -1:  
                assert False, f"Célula ({row}, {col}) não contém uma bomba"
    assert True


def test_bombs_game_hard_is_bigger(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)

    bombs_test = 120

    assert bombs_test > game.bombs

def test_bombs_game_hard_is_smaller(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)

    bombs_test = 50

    assert bombs_test < game.bombs

def test_bombs_game_hard_is_correct(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)

    bombs_test = 100

    assert bombs_test == game.bombs


def test_board_contains_only_bombs_hard(root):
    show_difficulty_menu_function(root, show_game)
    game = start_game(24, 24, 576, root, show_difficulty_menu_function(root, show_game))


    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] != -1:  
                assert False, f"Célula ({row}, {col}) não contém uma bomba"

    assert True


def test_board_has_no_bombs_easy(root):
    show_difficulty_menu_function(root, show_game)
    game = start_game(8, 8, 0, root, show_difficulty_menu_function(root, show_game))

    
    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] == -1:  
                assert False, f"Célula ({row}, {col}) contém uma bomba"

    assert True


def test_board_has_no_bombs_mid(root):
    show_difficulty_menu_function(root, show_game)
    game = start_game(10, 16, 0, root, show_difficulty_menu_function(root, show_game))

    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] == -1: 
                assert False, f"Célula ({row}, {col}) contém uma bomba"

    assert True


def test_board_has_no_bombs_hard(root):
    show_difficulty_menu_function(root, show_game)
    game = start_game(24, 24, 0, root, show_difficulty_menu_function(root, show_game))

    
    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] == -1:  
                assert False, f"Célula ({row}, {col}) contém uma bomba"

    assert True


def test_bombs_are_valid_in_easy_board(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    rows = 8
    cols = 8
    bombs = 10


    for row in range(rows):
        for col in range(cols):
            if game.field[row][col] == -1:
                assert 0 <= row < rows and 0 <= col < cols, f"Célula ({row}, {col}) contém uma bomba fora dos limites"
    assert True


def test_bombs_are_valid_in_mid_board(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)

    rows = 10
    cols = 16
    bombs = 30

    for row in range(rows):
        for col in range(cols):
            if game.field[row][col] == -1:  
                assert 0 <= row < rows and 0 <= col < cols, f"Célula ({row}, {col}) contém uma bomba fora dos limites"

    assert True


def test_bombs_are_valid_in_hard_board(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)

    rows = 24
    cols = 24
    bombs = 100

    for row in range(rows):
        for col in range(cols):
            if game.field[row][col] == -1: 
                assert 0 <= row < rows and 0 <= col < cols, f"Célula ({row}, {col}) contém uma bomba fora dos limites"


def test_board_has_at_least_one_bomb_in_hard_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)

    bomb_found = False 
    
    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] == -1:  
                bomb_found = True
                break  
    assert bomb_found, "Nenhuma bomba foi encontrada no tabuleiro"


def test_board_has_at_least_one_bomb_in_easy_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    bomb_found = False 

    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] == -1: 
                bomb_found = True
                break  

    assert bomb_found, "Nenhuma bomba foi encontrada no tabuleiro"

def test_board_has_at_least_one_bomb_in_mid_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)

    bomb_found = False 

    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] == -1: 
                bomb_found = True
                break  

    assert bomb_found, "Nenhuma bomba foi encontrada no tabuleiro"


def test_negative_bomb_count_in_easy_game(root):
    show_difficulty_menu_function(root, show_game)
    game = start_game(8, 8, -1, root, show_difficulty_menu_function(root, show_game))
    bombs = game.bombs

    assert bombs < 0, f"O número de bombas ({bombs}) é negativo"

def test_negative_bomb_count_in_mid_game(root):
    show_difficulty_menu_function(root, show_game)
    game = start_game(10, 16, -1, root, show_difficulty_menu_function(root, show_game))
    bombs = game.bombs

    assert bombs < 0, f"O número de bombas ({bombs}) não é negativo"

def test_negative_bomb_count_in_hard_game(root):
    show_difficulty_menu_function(root, show_game)
    game = start_game(24, 24, -1, root, show_difficulty_menu_function(root, show_game))
    bombs = game.bombs

    assert bombs < 0, f"O número de bombas ({bombs}) não é negativo"

def test_valid_bomb_count_in_easy_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    bombs = game.bombs
   
    assert isinstance(bombs, int), f"O número de bombas ({bombs}) não é um inteiro válido"

def test_valid_bomb_count_in_mid_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)

    bombs = game.bombs

    assert isinstance(bombs, int), f"O número de bombas ({bombs}) não é um inteiro válido"

def test_valid_bomb_count_in_hard_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)

    bombs = game.bombs

    assert isinstance(bombs, int), f"O número de bombas ({bombs}) não é um inteiro válido"

def test_enough_spaces_for_bombs_in_easy_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    bombs = game.bombs
    total_cells = game.rows * game.cols

    empty_cells = sum(1 for row in range(game.rows) for col in range(game.cols) if game.field[row][col] != -1)

    assert empty_cells >= bombs, f"Não há espaços suficientes no tabuleiro para as bombas ({empty_cells} < {bombs})"


def test_enough_spaces_for_bombs_in_mid_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)

    bombs = game.bombs
    total_cells = game.rows * game.cols

    empty_cells = sum(1 for row in range(game.rows) for col in range(game.cols) if game.field[row][col] != -1)

    assert empty_cells >= bombs, f"Não há espaços suficientes no tabuleiro para as bombas ({empty_cells} < {bombs})"

def test_enough_spaces_for_bombs_in_hard_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)

    bombs = game.bombs
    total_cells = game.rows * game.cols

    empty_cells = sum(1 for row in range(game.rows) for col in range(game.cols) if game.field[row][col] != -1)

    assert empty_cells >= bombs, f"Não há espaços suficientes no tabuleiro para as bombas ({empty_cells} < {bombs})"

def test_valid_bomb_count_in_easy_game_str(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    bombs = game.bombs
   
    assert isinstance(bombs, str) is False

def test_valid_bomb_count_in_mid_game_str(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)

    bombs = game.bombs

    assert isinstance(bombs, str) is False

def test_valid_bomb_count_in_hard_game_str(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)

    bombs = game.bombs

    assert isinstance(bombs, str) is False

def test_valid_bomb_count_in_easy_game_boolean(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    bombs = game.bombs
   
    assert isinstance(bombs, bool) is False

def test_valid_bomb_count_in_mid_game_boolean(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)

    bombs = game.bombs

    assert isinstance(bombs, bool) is False

def test_valid_bomb_count_in_hard_game_boolean(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)

    bombs = game.bombs

    assert isinstance(bombs, bool) is False