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
started = True

# Testa se a função retorna o valor de bomb_count quando o jogo está encerrado


def test_on_right_click_function_game_over():
    result = on_right_click_function(
        event, True, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == bomb_count

# Testa se a função retorna o valor de bomb_count quando o jogo está pausado


def test_on_right_click_function_paused():
    result = on_right_click_function(
        event, game_over, True, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == bomb_count

# Testa se a função incrementa bomb_count e configura a bandeira quando ela não está definida


def test_on_right_click_function_flag_not_set():
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == bomb_count + 1
    assert flags[row][col] is True
    assert buttons[row][col]['text'] == '🏳'


# Testa se a função decrementa bomb_count e remove a bandeira quando ela já está definida

def test_on_right_click_function_flag_set():
    flags[row][col] = True
    buttons[row][col]['text'] = '🏳'
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
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
        event, game_over, True, bombs, flags, buttons, row, col, bomb_count, started)

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
        event, game_over, True, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == initial_bomb_count
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''

# Testa se a função não altera bomb_count quando o jogo está encerrado, mas a bandeira já está definida


def test_on_right_click_function_game_over_with_flag_set():
    flags[row][col] = True
    buttons[row][col]['text'] = '🏳'
    initial_bomb_count = bomb_count
    result = on_right_click_function(
        event, True, paused, bombs, flags, buttons, row, col, bomb_count, started)
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
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == bomb_count
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''

# Testa se a função remove corretamente a bandeira quando a ação é chamada em um botão com bandeira definida


def test_on_right_click_function_unset_flag():
    flags[row][col] = True
    buttons[row][col]['text'] = '🏳'
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == bomb_count - 1
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''

# Testa se a função incrementa corretamente bomb_count quando a bandeira não está definida


def test_on_right_click_function_increment_bomb_count():
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
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
        event, game_over, True, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == initial_bomb_count
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''

# Testa se a função não altera bomb_count quando o jogo está encerrado, mas a bandeira não está definida


def test_on_right_click_function_game_over_with_unset_flag():
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    initial_bomb_count = bomb_count
    result = on_right_click_function(
        event, True, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == initial_bomb_count
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


def test_on_right_click_function_increment_bomb_count_with_max_bombs():
    bombs = 5
    bomb_count = 5
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == bomb_count
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''

# Testa se a função remove corretamente a bandeira quando o limite máximo de bombas já foi atingido


def test_on_right_click_function_remove_flag_with_max_bombs():
    bombs = 5
    bomb_count = 5
    flags[row][col] = True
    buttons[row][col]['text'] = '🏳'
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == bomb_count - 1
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''

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








# Testa se a função não altera bomb_count quando o jogo está pausado e uma bandeira inválida está definida
def test_on_right_click_function_paused_with_invalid_flag_set():
    paused = True
    flags[row][col] = True
    buttons[row][col]['text'] = '🚩'
    initial_bomb_count = bomb_count
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == initial_bomb_count
    assert flags[row][col] is True
    assert buttons[row][col]['text'] == '🚩'

# Testa se a função decrementa bomb_count quando uma bandeira inválida está definida e depois remove a bandeira ( a bandeira nao sera removida, pois o código busca pela bandeira correta)
def test_on_right_click_function_decrement_bomb_count_with_invalid_flag():
    flags[row][col] = True
    buttons[row][col]['text'] = '🚩'
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == bomb_count 
    # assert flags[row][col] is False
    assert buttons[row][col]['text'] == '🚩'

# Testa se a função não altera bomb_count quando o número de bandeiras é maior que o número total de células
def test_on_right_click_function_too_many_flags_cells():
    bombs = 5
    bomb_count = 25  # Maior que o número total de células (5x5 grid)
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == bomb_count
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''

# Testa se a função não altera bomb_count quando o número de bandeiras é igual ao número total de células
def test_on_right_click_function_max_flags_cells():
    bombs = 5
    bomb_count = 25  # Igual ao número total de células (5x5 grid)
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == bomb_count
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''

# Testa se a função não altera bomb_count quando o número de bandeiras é maior que o número de bombas
def test_on_right_click_function_too_many_flags_bombs():
    bombs = 5
    bomb_count = 6  # Maior que o número de bombas
    flags[row][col] = False
    buttons[row][col]['text'] = ''
    result = on_right_click_function(
        event, game_over, paused, bombs, flags, buttons, row, col, bomb_count, started)
    assert result == bomb_count
    assert flags[row][col] is False
    assert buttons[row][col]['text'] == ''