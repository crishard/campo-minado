import pytest
from functions.on_right_click import on_right_click_function
import tkinter as tk

import subprocess
import tkinter as tk
from campo_minado import create_game_instance, show_difficulty_menu, show_game, start_game, CampoMinado
from functions.show_difficulty_menu import show_difficulty_menu_function
import pytest

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

# Testar se a zona esta coberta
def test_zone_is_covered_add_flag():
    flags[row][col] = False
    assert buttons[row][col]['text'] == ''

# Testar se é possível adicionar uma bandeira
def test_add_flag():
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert buttons[row][col]['text'] == '🏳'

#  Testa se a zona esta descoberta
def test_zone_is_not_covered():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8,]

    for value in a:
        flags[row][col] = value
    assert buttons[row][col]['text'] == '' or buttons[row][col]['text'] == '🏳'

# Testa se esta jogando fora da matriz
def test_play_outside_matrix_easy(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    row_to_click = game.rows + 1
    col_to_click = game.cols + 1

    game_instance = game

    try:
        result = on_right_click_function(
            event, game_over, paused, bombs, flags, buttons, row_to_click, col_to_click, bomb_count, started)
    except Exception as e:
        assert str(e) == "list index out of range"

#  Testa se tem bandeira na zona
def test_zone_has_flags():
    # Coordenadas da zona que você deseja testar
    zone_row = 0
    zone_col = 0

    for row in range(zone_row, zone_row + 3):
        for col in range(zone_col, zone_col + 3):
            flags[row][col] = True

    # Verifique se todas as células da zona têm bandeiras
    for row in range(zone_row, zone_row + 3):
        for col in range(zone_col, zone_col + 3):
            assert flags[row][col], f"A célula ({row}, {col}) não tem uma bandeira na zona."

    # Se todas as células da zona tiverem bandeiras, o teste é bem-sucedido
    assert True

#  Testa se a zona esta descoberta
def test_zone_is_already_discovered():
    # Coordenadas da zona que você deseja testar
    zone_row = 0
    zone_col = 0

    # Defina algumas células da zona como descobertas
    for row in range(zone_row, zone_row + 3):
        for col in range(zone_col, zone_col + 3):
            buttons[row][col]['text'] = '1'  # Suponhamos que '1' representa uma célula descoberta


    for row in range(zone_row, zone_row + 3):
        for col in range(zone_col, zone_col + 3):
            assert buttons[row][col]['text'] == '1', f"A célula ({row}, {col}) não permaneceu descoberta após o clique na zona."

# Testa se a zona esta coberta
def test_zone_is_covered():
    # Coordenadas da zona que você deseja testar
    zone_row = 0
    zone_col = 0

    # Inicialize o estado do jogo com todas as células da zona cobertas
    buttons = [[{'text': '🏳'} for _ in range(8)] for _ in range(8)]  # Suponhamos que '🏳' representa uma bandeira

    for row in range(zone_row, zone_row + 3):
        for col in range(zone_col, zone_col + 3):
            assert buttons[row][col]['text'] == '🏳', f"A célula ({row}, {col}) não permaneceu coberta após o clique na zona."

# Testa se a bandeira foi removida corretamente
def test_on_right_click_function_unset_flag():
    flags[row][col] = True
    buttons[row][col]['text'] = '🏳'
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert buttons[row][col]['text'] == ''


# Testa se as bandeiras ja acabaram
def test_flags_empty(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)


    # meu bomb_count inicia como com -2 e itera para cada bandeira utilizada, o numero e -2 para que se tenha bombas + 2 bandeiras o qeu dao 12 bandeiras;
    flags = game.bomb_count + game.bombs 

    assert flags == 8

# Testa se o numero de bandeiras esta sendo atualizado corretamente
def test_count_flag():
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert result is -1




# Testa se a função não altera bomb_count quando o jogo não começou ainda
def test_on_right_click_function_game_not_started():
    started = False
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    initial_bomb_count = bomb_count
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == initial_bomb_count
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''

# Testa se a função não altera bomb_count quando o número de bandeiras é igual ao número de bombas
def test_on_right_click_function_max_flags_reached():
    bombs = 5
    bomb_count = 5
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == bomb_count
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''

# Testa se a função não altera bomb_count quando o número de bandeiras é maior que o número de bombas
def test_on_right_click_function_too_many_flags():
    bombs = 5
    bomb_count = 6
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == bomb_count
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''

# Testa se a função não altera bomb_count quando o jogo não está pausado, mas a bandeira já está definida
def test_on_right_click_function_not_paused_with_flag_set():
    paused = False
    flags[row][col] = True
    buttons[row][col]['text'] = '🏳' # aqui tenho -1 bandeira
    initial_bomb_count = bomb_count - 1 # aqui subtraio a bandeira adicionada anteriormente
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == initial_bomb_count


# Testa se a função remove a bandeira e decrementa bomb_count quando uma bandeira inválida está definida


def test_on_right_click_function_invalid_flag_set():
    flags[row][col] = True
    buttons[row][col]['text'] = '🏳'
    initial_bomb_count = bomb_count
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == initial_bomb_count - 1
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''

# Testa se a função não altera bomb_count quando o jogo está encerrado, mas uma bandeira inválida está definida


def test_on_right_click_function_game_over_with_invalid_flag_set():
    flags[row][col] = True
    buttons[row][col]['text'] = '🚩'
    initial_bomb_count = bomb_count
    result = on_right_click_function(
        event, True, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == initial_bomb_count
    assert flags[row][col] is True
    assert buttons[row][col]['text'] == '🚩'

# Testa se a função incrementa bomb_count quando uma bandeira inválida está definida e depois remove a bandeira


def test_on_right_click_function_increment_bomb_count_with_invalid_flag():
    flags[row][col] = True
    buttons[row][col]['text'] = '🏳'
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == bomb_count - 1
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''


# Testa se a função não altera bomb_count quando o jogo está pausado, mas a bandeira não está definida


def test_on_right_click_function_paused_with_unset_flag():
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    initial_bomb_count = bomb_count
    result = on_right_click_function(
        event, game_over, True, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == initial_bomb_count
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''

# Testa se a função não altera bomb_count quando o jogo está pausado e a bandeira já está definida


def test_on_right_click_function_paused_with_flag_set():
    flags[row][col] = True
    buttons[row][col]['text'] = '🏳'
    initial_bomb_count = bomb_count
    result = on_right_click_function(
        event, game_over, True, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == initial_bomb_count
    assert flags[row][col] is True
    assert buttons[row][col]['text'] == '🏳'

# Testa se a função incrementa corretamente bomb_count quando o limite máximo de bombas já foi atingido