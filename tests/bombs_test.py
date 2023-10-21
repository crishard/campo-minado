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

    # Verifica se todas as células do tabuleiro contêm bombas
    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] != -1:  # Se a célula não contém uma bomba
                assert False, f"Célula ({row}, {col}) não contém uma bomba"

    # Se todas as células foram verificadas e nenhuma falha ocorreu, o teste passou
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

    # Verifica se todas as células do tabuleiro contêm bombas
    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] != -1:  # Se a célula não contém uma bomba
                assert False, f"Célula ({row}, {col}) não contém uma bomba"

    # Se todas as células foram verificadas e nenhuma falha ocorreu, o teste passou
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

    # Verifica se todas as células do tabuleiro contêm bombas
    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] != -1:  # Se a célula não contém uma bomba
                assert False, f"Célula ({row}, {col}) não contém uma bomba"

    # Se todas as células foram verificadas e nenhuma falha ocorreu, o teste passou
    assert True


def test_board_has_no_bombs_easy(root):
    show_difficulty_menu_function(root, show_game)
    game = start_game(8, 8, 0, root, show_difficulty_menu_function(root, show_game))

    # Verifica se não há bombas em nenhuma célula do tabuleiro
    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] == -1:  # Se a célula contém uma bomba
                assert False, f"Célula ({row}, {col}) contém uma bomba"

    # Se todas as células foram verificadas e nenhuma falha ocorreu, o teste passou
    assert True


def test_board_has_no_bombs_mid(root):
    show_difficulty_menu_function(root, show_game)
    game = start_game(10, 16, 0, root, show_difficulty_menu_function(root, show_game))

    # Verifica se não há bombas em nenhuma célula do tabuleiro
    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] == -1:  # Se a célula contém uma bomba
                assert False, f"Célula ({row}, {col}) contém uma bomba"

    # Se todas as células foram verificadas e nenhuma falha ocorreu, o teste passou
    assert True


def test_board_has_no_bombs_hard(root):
    show_difficulty_menu_function(root, show_game)
    game = start_game(24, 24, 0, root, show_difficulty_menu_function(root, show_game))

    # Verifica se não há bombas em nenhuma célula do tabuleiro
    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] == -1:  # Se a célula contém uma bomba
                assert False, f"Célula ({row}, {col}) contém uma bomba"

    # Se todas as células foram verificadas e nenhuma falha ocorreu, o teste passou
    assert True


def test_bombs_are_valid_in_easy_board(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    # Defina as dimensões do tabuleiro fácil
    rows = 8
    cols = 8
    bombs = 10

    # Verifica se o número de bombas corresponde ao número esperado
    assert bombs == game.bombs, f"O número de bombas ({game.bombs}) não corresponde ao esperado ({bombs})"

    # Verifica se as coordenadas das bombas estão dentro dos limites do tabuleiro
    for row in range(rows):
        for col in range(cols):
            if game.field[row][col] == -1:  # Se a célula contém uma bomba
                assert 0 <= row < rows and 0 <= col < cols, f"Célula ({row}, {col}) contém uma bomba fora dos limites"

    # Se todas as verificações passaram, o teste é bem-sucedido
    assert True


def test_bombs_are_valid_in_mid_board(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)

    # Defina as dimensões do tabuleiro fácil
    rows = 10
    cols = 16
    bombs = 30

    # Verifica se o número de bombas corresponde ao número esperado
    assert bombs == game.bombs, f"O número de bombas ({game.bombs}) não corresponde ao esperado ({bombs})"

    # Verifica se as coordenadas das bombas estão dentro dos limites do tabuleiro
    for row in range(rows):
        for col in range(cols):
            if game.field[row][col] == -1:  # Se a célula contém uma bomba
                assert 0 <= row < rows and 0 <= col < cols, f"Célula ({row}, {col}) contém uma bomba fora dos limites"

    # Se todas as verificações passaram, o teste é bem-sucedido
    assert True


def test_bombs_are_valid_in_hard_board(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)

    # Defina as dimensões do tabuleiro fácil
    rows = 24
    cols = 24
    bombs = 100

    # Verifica se o número de bombas corresponde ao número esperado
    assert bombs == game.bombs, f"O número de bombas ({game.bombs}) não corresponde ao esperado ({bombs})"

    # Verifica se as coordenadas das bombas estão dentro dos limites do tabuleiro
    for row in range(rows):
        for col in range(cols):
            if game.field[row][col] == -1:  # Se a célula contém uma bomba
                assert 0 <= row < rows and 0 <= col < cols, f"Célula ({row}, {col}) contém uma bomba fora dos limites"


def test_board_has_at_least_one_bomb_in_hard_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)

    bomb_found = False  # Inicialmente, nenhuma bomba foi encontrada

    # Verifica se há pelo menos uma bomba no tabuleiro
    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] == -1:  # Se a célula contém uma bomba
                bomb_found = True
                break  # Sai do loop assim que uma bomba for encontrada

    # Verifica se uma bomba foi encontrada
    assert bomb_found, "Nenhuma bomba foi encontrada no tabuleiro"


def test_board_has_at_least_one_bomb_in_easy_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    bomb_found = False  # Inicialmente, nenhuma bomba foi encontrada

    # Verifica se há pelo menos uma bomba no tabuleiro
    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] == -1:  # Se a célula contém uma bomba
                bomb_found = True
                break  # Sai do loop assim que uma bomba for encontrada

    # Verifica se uma bomba foi encontrada
    assert bomb_found, "Nenhuma bomba foi encontrada no tabuleiro"

def test_board_has_at_least_one_bomb_in_mid_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)

    bomb_found = False  # Inicialmente, nenhuma bomba foi encontrada

    # Verifica se há pelo menos uma bomba no tabuleiro
    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] == -1:  # Se a célula contém uma bomba
                bomb_found = True
                break  # Sai do loop assim que uma bomba for encontrada

    # Verifica se uma bomba foi encontrada
    assert bomb_found, "Nenhuma bomba foi encontrada no tabuleiro"


def test_negative_bomb_count_in_easy_game(root):
    show_difficulty_menu_function(root, show_game)
    game = start_game(8, 8, -1, root, show_difficulty_menu_function(root, show_game))
    bombs = game.bombs

    # Verifica se o número de bombas é negativo
    assert bombs < 0, f"O número de bombas ({bombs}) é negativo"



def test_negative_bomb_count_in_mid_game(root):
    show_difficulty_menu_function(root, show_game)
    game = start_game(10, 16, -1, root, show_difficulty_menu_function(root, show_game))
    bombs = game.bombs

    # Verifica se o número de bombas é negativo
    assert bombs < 0, f"O número de bombas ({bombs}) não é negativo"



def test_negative_bomb_count_in_hard_game(root):
    show_difficulty_menu_function(root, show_game)
    game = start_game(24, 24, -1, root, show_difficulty_menu_function(root, show_game))
    bombs = game.bombs

    # Verifica se o número de bombas é negativo
    assert bombs < 0, f"O número de bombas ({bombs}) não é negativo"


def test_valid_bomb_count_in_easy_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    bombs = game.bombs

    # Verifica se o número de bombas é um inteiro válido
    assert isinstance(bombs, int), f"O número de bombas ({bombs}) não é um inteiro válido"

def test_valid_bomb_count_in_mid_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)

    bombs = game.bombs

    # Verifica se o número de bombas é um inteiro válido
    assert isinstance(bombs, int), f"O número de bombas ({bombs}) não é um inteiro válido"

def test_valid_bomb_count_in_hard_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)

    bombs = game.bombs

    # Verifica se o número de bombas é um inteiro válido
    assert isinstance(bombs, int), f"O número de bombas ({bombs}) não é um inteiro válido"



def test_enough_spaces_for_bombs_in_easy_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    # Obtém o número de bombas e o tamanho do tabuleiro
    bombs = game.bombs
    total_cells = game.rows * game.cols

    # Conta o número de espaços disponíveis (células sem bombas)
    empty_cells = sum(1 for row in range(game.rows) for col in range(game.cols) if game.field[row][col] != -1)

    # Verifica se existem espaços suficientes para as bombas
    assert empty_cells >= bombs, f"Não há espaços suficientes no tabuleiro para as bombas ({empty_cells} < {bombs})"


def test_enough_spaces_for_bombs_in_mid_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)

    # Obtém o número de bombas e o tamanho do tabuleiro
    bombs = game.bombs
    total_cells = game.rows * game.cols

    # Conta o número de espaços disponíveis (células sem bombas)
    empty_cells = sum(1 for row in range(game.rows) for col in range(game.cols) if game.field[row][col] != -1)

    # Verifica se existem espaços suficientes para as bombas
    assert empty_cells >= bombs, f"Não há espaços suficientes no tabuleiro para as bombas ({empty_cells} < {bombs})"

def test_enough_spaces_for_bombs_in_hard_game(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)

    # Obtém o número de bombas e o tamanho do tabuleiro
    bombs = game.bombs
    total_cells = game.rows * game.cols

    # Conta o número de espaços disponíveis (células sem bombas)
    empty_cells = sum(1 for row in range(game.rows) for col in range(game.cols) if game.field[row][col] != -1)

    # Verifica se existem espaços suficientes para as bombas
    assert empty_cells >= bombs, f"Não há espaços suficientes no tabuleiro para as bombas ({empty_cells} < {bombs})"

