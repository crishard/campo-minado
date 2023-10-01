import pytest
from functions.on_right_click import on_right_click_function
import tkinter as tk

event = None
game_over = False
paused = False
bombs = 10
flags = [[False for _ in range(10)] for _ in range(10)]
buttons = [[tk.Button() for _ in range(10)] for _ in range(10)]
row = 5
col = 5
bomb_count = -2

# Testa se a função retorna o valor de bomb_count quando o jogo está encerrado


def test_on_right_click_function_game_over():
    result = on_right_click_function(
        event, True, paused, bombs, flags, buttons, row, col, bomb_count)
    assert result == bomb_count

# Testa se a função retorna o valor de bomb_count quando o jogo está pausado


def test_on_right_click_function_paused():
    result = on_right_click_function(
        event, game_over, True, bombs, flags, buttons, row, col, bomb_count)
    assert result == bomb_count

# Testa se a função incrementa bomb_count e configura a bandeira quando ela não está definida


def test_on_right_click_function_flag_not_set():
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count)
    assert result == bomb_count + 1
    assert flags[row][col] is True
    assert buttons[row][col]['text'] == '🏳'


# Testa se a função decrementa bomb_count e remove a bandeira quando ela já está definida

def test_on_right_click_function_flag_set():
    flags[row][col] = True
    buttons[row][col]['text'] = '🏳'
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count)
    assert result == bomb_count - 1
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''

# Testa se a função não faz nada quando todas as bandeiras estão definidas


def test_on_right_click_function_all_flags_set():
    for i in range(len(flags)):
        for j in range(len(flags[i])):
            flags[i][j] = True
            buttons[i][j]['text'] = '🏳'

    result = on_right_click_function(
        event, game_over, True, bombs, flags, buttons, row, col, bomb_count)

    assert result == bomb_count
    assert flags[row][col] is True
    assert buttons[row][col]['text'] == '🏳'

# Testa se a função não altera o estado quando as coordenadas estão fora dos limites


def test_on_right_click_function_invalid_coordinates():
    row = -1
    col = -1
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    initial_bomb_count = bomb_count
    result = on_right_click_function(
        event, game_over, True, bombs, flags, buttons, row, col, bomb_count)
    assert result == initial_bomb_count
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''

# Testa se a função não altera bomb_count quando o jogo está encerrado, mas a bandeira já está definida


def test_on_right_click_function_game_over_with_flag_set():
    flags[row][col] = True
    buttons[row][col]['text'] = '🏳'
    initial_bomb_count = bomb_count
    result = on_right_click_function(
        event, True, paused, bombs, flags, buttons, row, col, bomb_count)
    assert result == initial_bomb_count
    assert flags[row][col] is True
    assert buttons[row][col]['text'] == '🏳'

# Testa se a função não permite configurar mais bandeiras quando o limite é atingido


def test_on_right_click_function_max_bombs_reached():
    bombs = 5
    bomb_count = 5
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count)
    assert result == bomb_count
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''

# Testa se a função remove corretamente a bandeira quando a ação é chamada em um botão com bandeira definida


def test_on_right_click_function_unset_flag():
    flags[row][col] = True
    buttons[row][col]['text'] = '🏳'
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count)
    assert result == bomb_count - 1
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''

# Testa se a função incrementa corretamente bomb_count quando a bandeira não está definida


def test_on_right_click_function_increment_bomb_count():
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count)
    assert result == bomb_count + 1
    assert flags[row][col] is True
    assert buttons[row][col]['text'] == '🏳'

# Testa se a função não altera o estado quando as coordenadas estão dentro dos limites válidos


def test_on_right_click_function_valid_coordinates():
    row = 3
    col = 7
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    initial_bomb_count = bomb_count
    result = on_right_click_function(
        event, game_over, True, bombs, flags, buttons, row, col, bomb_count)
    assert result == initial_bomb_count
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''

# Testa se a função não altera bomb_count quando o jogo está encerrado, mas a bandeira não está definida


def test_on_right_click_function_game_over_with_unset_flag():
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    initial_bomb_count = bomb_count
    result = on_right_click_function(
        event, True, paused, bombs, flags, buttons, row, col, bomb_count)
    assert result == initial_bomb_count
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''
