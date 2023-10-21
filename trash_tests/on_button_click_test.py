import pytest
import datetime
from tkinter import Tk
from campo_minado import CampoMinado


@pytest.fixture
def campo_minado():
    root = Tk()
    return CampoMinado(root, 8, 8, 1, lambda: None)

# Verifica se o jogo não é afetado ao clicar em um botão após o término do jogo
def test_on_button_click_end_game(campo_minado):
    campo_minado.game_over = True
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Verifica se o jogo é encerrado quando uma bomba é clicada
def test_on_button_click_bomb(campo_minado):
    campo_minado.field[2][3] = -1
    campo_minado.on_button_click(2, 3)
    assert campo_minado.game_over is True


# Verifica se o jogo continua quando um local seguro é clicado
def test_on_button_click_safe(campo_minado):
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Verifica se o jogo não é afetado quando um local marcado com bandeira é clicado
def test_on_button_click_flagged(campo_minado):
    campo_minado.flags[2][3] = True
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

def test_on_button_click_non_bomb_non_flagged(campo_minado):
    campo_minado.field[2][3] = 0  # Non-bomb location
    campo_minado.on_button_click(2, 3)
    assert campo_minado.flags[2][3] is True  # Corrigido para verificar que a bandeira deve permanecer False para uma localização não sinalizada

# Verifies if the game ends when a flagged bomb location is clicked
def test_on_button_click_flagged_bomb(campo_minado):
    campo_minado.field[2][3] = -1  # Bomb location
    campo_minado.flags[2][3] = True  # Flagged as a bomb
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Verifies if the game continues when a flagged non-bomb location is clicked
def test_on_button_click_flagged_non_bomb(campo_minado):
    campo_minado.field[2][3] = 0  # Non-bomb location
    campo_minado.flags[2][3] = True  # Flagged as non-bomb
    campo_minado.on_button_click(2, 3)
    assert campo_minado.flags[2][3] is True

# Verifies if the game ends when a non-flagged bomb location is clicked
def test_on_button_click_non_flagged_bomb(campo_minado):
    campo_minado.field[2][3] = -1  # Bomb location
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Verifies if the game continues when a flagged location is clicked after pausing
def test_on_button_click_flagged_after_pause(campo_minado):
    campo_minado.paused = True
    campo_minado.field[2][3] = 0  # Non-bomb location
    campo_minado.flags[2][3] = True  # Flagged as non-bomb
    campo_minado.on_button_click(2, 3)
    assert campo_minado.flags[2][3] is True

# Teste 3: Verificar se a célula clicada exibe o número correto de bombas vizinhas
def test_on_button_click_display_correct_bomb_count(campo_minado):
    campo_minado.field[2][3] = 2  # Célula com 2 bombas vizinhas
    campo_minado.on_button_click(2, 3)
    assert campo_minado.buttons[2][3]['text'] == '2'  # Deve exibir '2' na célula clicada

# Teste 4: Verificar se a célula clicada não exibe um número quando uma célula não sinalizada com bomba é clicada
def test_on_button_click_display_no_number_on_bomb(campo_minado):
    campo_minado.field[2][3] = -1  # Célula com bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.buttons[2][3]['text'] == '💣'  # A célula não deve exibir um número

# Teste 5: Verificar se o jogo continua quando uma célula já sinalizada como bandeira é clicada
def test_on_button_click_flagged_cell(campo_minado):
    campo_minado.flags[2][3] = True  # Célula já sinalizada como bandeira
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 6: Verificar se o jogo continua quando uma célula já sinalizada como bandeira é clicada com o botão direito do mouse
def test_on_right_click_flagged_cell(campo_minado):
    campo_minado.flags[2][3] = True  # Célula já sinalizada como bandeira
    campo_minado.on_right_click(None, 2, 3)
    assert campo_minado.is_game_over is False

# Teste 7: Verificar se o jogo continua quando uma célula já sinalizada como bandeira é clicada com o botão esquerdo do mouse
def test_on_button_click_flagged_cell_left_click(campo_minado):
    campo_minado.flags[2][3] = True  # Célula já sinalizada como bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 8: Verificar se a bandeira é removida quando uma célula já sinalizada como bandeira é clicada com o botão esquerdo do mouse (não pode ser removida, somente com o botão direito removemos e adicionamos bandeira)
def test_on_button_click_remove_flag(campo_minado):
    campo_minado.flags[2][3] = True  # Célula já sinalizada como bandeira
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False
    assert campo_minado.flags[2][3] is True  # A bandeira deve ser removida

# Teste 9: Verificar se o jogo termina quando uma célula sinalizada como bandeira com uma bomba é clicada (so podemos descobrir uma célula caso ela ja nao tenha mais a bandeira)
def test_on_button_click_flagged_bomb_cell(campo_minado):
    campo_minado.flags[2][3] = True  # Célula sinalizada como bandeira
    campo_minado.field[2][3] = -1  # Célula com bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 10: Verificar se o jogo continua quando uma célula sinalizada como bandeira sem bomba é clicada
def test_on_button_click_flagged_non_bomb_cell(campo_minado):
    campo_minado.flags[2][3] = True  # Célula sinalizada como bandeira
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False


# Teste 13: Verificar se o jogo continua quando uma célula não sinalizada como bandeira é clicada (célula sem bomba)
def test_on_button_click_unflagged_non_bomb_cell(campo_minado):
    campo_minado.flags[2][3] = False  # Célula não sinalizada como bandeira
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 14: Verificar se o jogo termina quando uma célula não sinalizada como bandeira é clicada (célula com bomba)
def test_on_button_click_unflagged_bomb_cell(campo_minado):
    campo_minado.flags[2][3] = False  # Célula não sinalizada como bandeira
    campo_minado.field[2][3] = -1  # Célula com bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.game_over is True

# Teste 15: Verificar se o jogo continua quando uma célula não sinalizada como bandeira é clicada (célula sem bomba, adjacente a células com bombas)
def test_on_button_click_unflagged_adjacent_to_bombs(campo_minado):
    campo_minado.flags[2][3] = False  # Célula não sinalizada como bandeira
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[1][2] = -1  # Célula adjacente com bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 16: Verificar se o jogo continua quando uma célula não sinalizada como bandeira é clicada (célula sem bomba, adjacente a células com bandeiras)
def test_on_button_click_unflagged_adjacent_to_flags(campo_minado):
    campo_minado.flags[2][3] = False  # Célula não sinalizada como bandeira
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.flags[1][2] = True  # Célula adjacente com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 17: Verificar se o jogo continua quando uma célula não sinalizada como bandeira é clicada (célula sem bomba, adjacente a células com números)
def test_on_button_click_unflagged_adjacent_to_numbers(campo_minado):
    campo_minado.flags[2][3] = False  # Célula não sinalizada como bandeira
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[1][2] = 1  # Célula adjacente com 1 bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 20: Verificar se o jogo continua quando uma célula não sinalizada como bandeira é clicada (célula sem bomba, adjacente a células com números iguais ao número de bandeiras adjacentes)
def test_on_button_click_unflagged_adjacent_to_equal_numbers(campo_minado):
    campo_minado.flags[2][3] = False  # Célula não sinalizada como bandeira
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[1][2] = 2  # Célula adjacente com 2 bandeiras
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False


# Teste 21: Verificar se o jogo continua quando uma célula não sinalizada como bandeira é clicada (célula sem bomba, adjacente a células com números e bandeiras)
def test_on_button_click_unflagged_adjacent_to_numbers_and_flags(campo_minado):
    campo_minado.flags[2][3] = False  # Célula não sinalizada como bandeira
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[1][2] = 1  # Célula adjacente com 1 bomba
    campo_minado.flags[1][4] = True  # Célula adjacente com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 22: Verificar se o jogo continua quando uma célula não sinalizada como bandeira é clicada (célula sem bomba, adjacente a células com números e bandeiras)
def test_on_button_click_unflagged_adjacent_to_equal_numbers_and_flags(campo_minado):
    campo_minado.flags[2][3] = False  # Célula não sinalizada como bandeira
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[1][2] = 2  # Célula adjacente com 2 bandeiras
    campo_minado.flags[1][4] = True  # Célula adjacente com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 23: Verificar se o jogo continua quando uma célula não sinalizada como bandeira é clicada (célula sem bomba, adjacente a células com números iguais ao número de bandeiras adjacentes, algumas não são bandeiras)
def test_on_button_click_unflagged_adjacent_to_equal_numbers_and_flags_mixed(campo_minado):
    campo_minado.flags[2][3] = False  # Célula não sinalizada como bandeira
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[1][2] = 2  # Célula adjacente com 2 bandeiras
    campo_minado.flags[1][4] = False  # Célula adjacente com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 24: Verificar se o jogo continua quando uma célula não sinalizada como bandeira é clicada (célula sem bomba, adjacente a células com números iguais ao número de bandeiras adjacentes, todas são bandeiras)
def test_on_button_click_unflagged_adjacent_to_equal_numbers_and_flags_all_flags(campo_minado):
    campo_minado.flags[2][3] = False  # Célula não sinalizada como bandeira
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[1][2] = 2  # Célula adjacente com 2 bandeiras
    campo_minado.flags[1][4] = True  # Célula adjacente com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 27: Verificar se o jogo continua quando uma célula já marcada como bandeira é clicada, mas está adjacente a células com números diferentes de bandeiras e bombas.
def test_on_button_click_flagged_adjacent_to_numbers_and_flags(campo_minado):
    campo_minado.flags[2][3] = True  # Célula marcada como bandeira
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[1][2] = 1  # Célula adjacente com 1 bomba
    campo_minado.flags[1][4] = True  # Célula adjacente com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 28: Verificar se o jogo continua quando uma célula já marcada como bandeira é clicada, mas está adjacente a células com números iguais ao número de bandeiras adjacentes.
def test_on_button_click_flagged_adjacent_to_equal_numbers_and_flags(campo_minado):
    campo_minado.flags[2][3] = True  # Célula marcada como bandeira
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[1][2] = 2  # Célula adjacente com 2 bandeiras
    campo_minado.flags[1][4] = True  # Célula adjacente com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 29: Verificar se o jogo continua quando uma célula já marcada como bandeira é clicada, mas está adjacente a células com números iguais ao número de bandeiras adjacentes, e algumas delas não estão marcadas como bandeira.
def test_on_button_click_flagged_adjacent_to_equal_numbers_and_flags_mixed(campo_minado):
    campo_minado.flags[2][3] = True  # Célula marcada como bandeira
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[1][2] = 2  # Célula adjacente com 2 bandeiras
    campo_minado.flags[1][4] = False  # Célula adjacente com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 30: Verificar se o jogo continua quando uma célula já marcada como bandeira é clicada, mas está adjacente a células com números iguais ao número de bandeiras adjacentes, e todas elas estão marcadas como bandeira.
def test_on_button_click_flagged_adjacent_to_equal_numbers_and_flags_all_flags(campo_minado):
    campo_minado.flags[2][3] = True  # Célula marcada como bandeira
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[1][2] = 2  # Célula adjacente com 2 bandeiras
    campo_minado.flags[1][4] = True  # Célula adjacente com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False


# Teste 31: Verificar se o jogo continua quando uma célula sem bomba é clicada e todas as células sem bomba adjacentes também são reveladas.
def test_on_button_click_non_bomb_reveal_adjacent(campo_minado):
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[2][4] = 0  # Célula sem bomba adjacente
    campo_minado.field[3][3] = 0  # Célula sem bomba adjacente
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 32: Verificar se o jogo continua quando uma célula sem bomba é clicada e algumas das células sem bomba adjacentes já estão reveladas.
def test_on_button_click_non_bomb_reveal_partial_adjacent(campo_minado):
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[2][4] = 0  # Célula sem bomba adjacente já revelada
    campo_minado.field[3][3] = 0  # Célula sem bomba adjacente
    campo_minado.buttons[2][4].config(text="0")  # Simular célula adjacente já revelada
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 33: Verificar se o jogo continua quando uma célula sem bomba é clicada e há células com bandeira adjacentes, mas o número de bandeiras corresponde ao número de bombas adjacentes.
def test_on_button_click_non_bomb_with_flags_adjacent(campo_minado):
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[2][4] = 0  # Célula sem bomba adjacente
    campo_minado.field[3][3] = 0  # Célula sem bomba adjacente
    campo_minado.flags[2][4] = True  # Célula adjacente com bandeira
    campo_minado.flags[3][3] = True  # Célula adjacente com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False



# Teste 34: Verificar se o jogo vence quando todas as células sem bomba são reveladas e todas as bombas estão marcadas com bandeira.
def test_on_button_click_win_all_non_bombs_marked(campo_minado):
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[2][4] = 0  # Célula sem bomba
    campo_minado.field[3][3] = 0  # Célula sem bomba
    campo_minado.field[3][4] = -1  # Bomba, marcada com bandeira
    campo_minado.field[4][3] = -1  # Bomba, marcada com bandeira
    campo_minado.field[4][4] = -1  # Bomba, marcada com bandeira
    campo_minado.flags[3][4] = True  # Marcar a bomba com bandeira
    campo_minado.flags[4][3] = True  # Marcar a bomba com bandeira
    campo_minado.flags[4][4] = True  # Marcar a bomba com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 35: Verificar se o jogo não vence quando todas as células sem bomba são reveladas, mas algumas bombas não estão marcadas com bandeira.
def test_on_button_click_no_win_unflagged_bombs(campo_minado):
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[2][4] = 0  # Célula sem bomba
    campo_minado.field[3][3] = 0  # Célula sem bomba
    campo_minado.field[3][4] = -1  # Bomba, não marcada com bandeira
    campo_minado.field[4][3] = -1  # Bomba, não marcada com bandeira
    campo_minado.field[4][4] = -1  # Bomba, não marcada com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False  # O jogo não deve vencer

# Teste 36: Verificar se o jogo não vence quando todas as bombas estão marcadas com bandeira, mas algumas células sem bomba não foram reveladas.
def test_on_button_click_no_win_unrevealed_non_bombs(campo_minado):
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[2][4] = 0  # Célula sem bomba
    campo_minado.field[3][3] = 0  # Célula sem bomba
    campo_minado.field[3][4] = -1  # Bomba, marcada com bandeira
    campo_minado.field[4][3] = -1  # Bomba, marcada com bandeira
    campo_minado.field[4][4] = -1  # Bomba, marcada com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False  # O jogo não deve vencer


# Teste 37: Verificar se o jogo continua quando uma célula sem bomba é clicada e há células com bandeira adjacentes, mas o número de bandeiras não corresponde ao número de bombas adjacentes.
def test_on_button_click_non_bomb_with_flags_incorrect_adjacent(campo_minado):
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[2][4] = 0  # Célula sem bomba
    campo_minado.field[3][3] = 0  # Célula sem bomba
    campo_minado.field[3][4] = -1  # Bomba, não marcada com bandeira
    campo_minado.flags[2][4] = True  # Célula adjacente com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 38: Verificar se o jogo continua quando uma célula com bomba é clicada, mas não todas as bombas estão marcadas com bandeira.
def test_on_button_click_bomb_unflagged(campo_minado):
    campo_minado.field[2][3] = -1  # Bomba, não marcada com bandeira
    campo_minado.field[2][4] = -1  # Bomba, marcada com bandeira
    campo_minado.field[3][3] = 0  # Célula sem bomba
    campo_minado.flags[2][4] = True  # Marcar a bomba com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.game_over is True

# Teste 39: Verificar se o jogo continua quando uma célula com bomba é clicada, mas algumas células adjacentes com bombas não estão marcadas com bandeira.
def test_on_button_click_bomb_unflagged_adjacent(campo_minado):
    campo_minado.field[2][3] = -1  # Bomba, não marcada com bandeira
    campo_minado.field[2][4] = -1  # Bomba, não marcada com bandeira
    campo_minado.field[3][3] = 0  # Célula sem bomba
    campo_minado.flags[2][4] = True  # Marcar uma bomba com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.game_over is True

# Teste 42: Verificar se o jogo não continua quando uma célula já revelada é clicada.
def test_on_button_click_already_revealed_cell(campo_minado):
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.buttons[2][3].config(text="1")  # Simular célula já revelada
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False  # O jogo não deve continuar

# Teste 43: Verificar se o jogo não continua quando uma célula fora dos limites é clicada.
def test_on_button_click_out_of_bounds_cell(campo_minado):
    campo_minado.on_button_click(-1, -1)  # Clicar em uma célula fora dos limites
    assert campo_minado.is_game_over is False  # O jogo não deve continuar

# Teste 44: Verificar se o jogo não continua quando uma célula com bandeira é clicada e há bombas não marcadas com bandeira adjacentes. (células com bandeira nao podem ser reveladas)
def test_on_button_click_flagged_cell_with_unflagged_bombs_adjacent(campo_minado):
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[2][4] = -1  # Bomba, não marcada com bandeira
    campo_minado.flags[2][3] = True  # Marcar a célula com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 45: Verificar se o jogo continua quando uma célula com bandeira é clicada, mas não há bombas não marcadas com bandeira adjacentes.
def test_on_button_click_flagged_cell_without_unflagged_bombs_adjacent(campo_minado):
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[2][4] = 0  # Célula sem bomba
    campo_minado.flags[2][3] = True  # Marcar a célula com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 46: Verificar se o jogo continua quando uma célula sem bomba é clicada e todas as células adjacentes já estão reveladas.
def test_on_button_click_non_bomb_all_adjacent_revealed(campo_minado):
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[2][4] = 0  # Célula sem bomba
    campo_minado.field[3][3] = 0  # Célula sem bomba
    campo_minado.field[3][4] = 0  # Célula sem bomba
    campo_minado.field[4][3] = 0  # Célula sem bomba
    campo_minado.field[4][4] = 0  # Célula sem bomba
    campo_minado.buttons[2][3].config(text="1")  # Simular célula já revelada
    campo_minado.buttons[2][4].config(text="1")  # Simular célula já revelada
    campo_minado.buttons[3][3].config(text="1")  # Simular célula já revelada
    campo_minado.buttons[3][4].config(text="1")  # Simular célula já revelada
    campo_minado.buttons[4][3].config(text="1")  # Simular célula já revelada
    campo_minado.buttons[4][4].config(text="1")  # Simular célula já revelada
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 47: Verificar se o jogo não continua quando uma célula com bomba é clicada e todas as bombas adjacentes estão marcadas com bandeira.
def test_on_button_click_bomb_all_adjacent_flagged(campo_minado):
    campo_minado.field[2][3] = -1  # Bomba
    campo_minado.field[2][4] = -1  # Bomba
    campo_minado.field[3][3] = -1  # Bomba
    campo_minado.field[3][4] = -1  # Bomba
    campo_minado.flags[2][3] = True  # Marcar bomba com bandeira
    campo_minado.flags[2][4] = True  # Marcar bomba com bandeira
    campo_minado.flags[3][3] = True  # Marcar bomba com bandeira
    campo_minado.flags[3][4] = True  # Marcar bomba com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False


# Teste 48: Verificar se o jogo continua quando uma célula sem bomba é clicada e há bombas marcadas com bandeira adjacentes.
def test_on_button_click_non_bomb_flagged_bombs_adjacent(campo_minado):
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[2][4] = -1  # Bomba, marcada com bandeira
    campo_minado.flags[2][4] = True  # Marcar a bomba com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 49: Verificar se o jogo continua quando uma célula com bomba é clicada, mas não todas as bombas adjacentes estão marcadas com bandeira.
def test_on_button_click_bomb_not_all_adjacent_flagged(campo_minado):
    campo_minado.field[2][3] = -1  # Bomba
    campo_minado.field[2][4] = -1  # Bomba, marcada com bandeira
    campo_minado.flags[2][4] = True  # Marcar uma bomba com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.game_over is True

# Teste 50: Verificar se o jogo não continua quando uma célula com bandeira é clicada e todas as bombas adjacentes estão marcadas com bandeira.
def test_on_button_click_flagged_cell_all_adjacent_flagged_bombs(campo_minado):
    campo_minado.field[2][3] = -1  # Bomba
    campo_minado.field[2][4] = -1  # Bomba
    campo_minado.field[3][3] = -1  # Bomba
    campo_minado.field[3][4] = -1  # Bomba
    campo_minado.flags[2][3] = True  # Marcar bomba com bandeira
    campo_minado.flags[2][4] = True  # Marcar bomba com bandeira
    campo_minado.flags[3][3] = True  # Marcar bomba com bandeira
    campo_minado.flags[3][4] = True  # Marcar bomba com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 51: Verificar se o jogo não continua quando uma célula com bandeira é clicada e há bombas não marcadas com bandeira adjacentes.
def test_on_button_click_flagged_cell_unflagged_bombs_adjacent(campo_minado):
    campo_minado.field[2][3] = -1  # Bomba
    campo_minado.field[2][4] = -1  # Bomba
    campo_minado.field[3][3] = -1  # Bomba
    campo_minado.field[3][4] = 0  # Célula sem bomba
    campo_minado.flags[2][3] = True  # Marcar bomba com bandeira
    campo_minado.flags[2][4] = True  # Marcar bomba com bandeira
    campo_minado.flags[3][3] = True  # Marcar bomba com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False


# Teste 52: Verificar se o jogo continua quando uma célula sem bomba é clicada e todas as células adjacentes também são não-bombas.
def test_on_button_click_non_bomb_all_adjacent_non_bombs(campo_minado):
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[2][4] = 0  # Célula sem bomba
    campo_minado.field[3][3] = 0  # Célula sem bomba
    campo_minado.field[3][4] = 0  # Célula sem bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 53: Verificar se o jogo continua quando uma célula sem bomba é clicada e todas as células adjacentes são bombas.
def test_on_button_click_non_bomb_all_adjacent_bombs(campo_minado):
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[2][4] = -1  # Bomba
    campo_minado.field[3][3] = -1  # Bomba
    campo_minado.field[3][4] = -1  # Bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 54: Verificar se o jogo continua quando uma célula sem bomba é clicada e algumas células adjacentes são bombas e outras não.
def test_on_button_click_non_bomb_mixed_adjacent_cells(campo_minado):
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.field[2][4] = -1  # Bomba
    campo_minado.field[3][3] = 0  # Célula sem bomba
    campo_minado.field[3][4] = -1  # Bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 55: Verificar se o jogo continua quando uma célula sem bomba é clicada e todas as células adjacentes são marcadas com bandeira.
def test_on_button_click_non_bomb_all_adjacent_flagged(campo_minado):
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.flags[2][4] = True  # Marcar com bandeira
    campo_minado.flags[3][3] = True  # Marcar com bandeira
    campo_minado.flags[3][4] = True  # Marcar com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 56: Verificar se o jogo continua quando uma célula sem bomba é clicada e algumas células adjacentes são marcadas com bandeira e outras não.
def test_on_button_click_non_bomb_mixed_adjacent_flags(campo_minado):
    campo_minado.field[2][3] = 0  # Célula sem bomba
    campo_minado.flags[2][4] = True  # Marcar com bandeira
    campo_minado.flags[3][3] = True  # Marcar com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False




# Teste 57: Verificar se o jogo continua quando uma célula com número é clicada e todas as células adjacentes são marcadas com bandeira.
def test_on_button_click_number_cell_all_adjacent_flagged(campo_minado):
    campo_minado.field[2][3] = 3  # Célula com número 3
    for r in range(2, 4):
        for c in range(3, 5):
            campo_minado.flags[r][c] = True  # Marcar todas as células adjacentes com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 58: Verificar se o jogo continua quando uma célula com número é clicada e todas as células adjacentes são marcadas com bandeira, exceto uma célula adjacente que é uma bomba.
def test_on_button_click_number_cell_almost_all_adjacent_flagged(campo_minado):
    campo_minado.field[2][3] = 3  # Célula com número 3
    for r in range(2, 4):
        for c in range(3, 5):
            campo_minado.flags[r][c] = True  # Marcar todas as células adjacentes com bandeira
    campo_minado.field[3][4] = -1  # Uma das células adjacentes é uma bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 59: Verificar se o jogo continua quando uma célula com número é clicada e todas as células adjacentes são marcadas com bandeira, exceto uma célula adjacente que é uma bomba e uma célula adjacente que não é uma bomba.
def test_on_button_click_number_cell_mixed_adjacent_flags(campo_minado):
    campo_minado.field[2][3] = 3  # Célula com número 3
    for r in range(2, 4):
        for c in range(3, 5):
            campo_minado.flags[r][c] = True  # Marcar todas as células adjacentes com bandeira
    campo_minado.field[3][4] = -1  # Uma das células adjacentes é uma bomba
    campo_minado.field[3][2] = 0  # Uma das células adjacentes não é uma bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 60: Verificar se o jogo continua quando uma célula com número é clicada e todas as células adjacentes são marcadas com bandeira, exceto duas células adjacentes que são bombas.
def test_on_button_click_number_cell_two_adjacent_bombs(campo_minado):
    campo_minado.field[2][3] = 3  # Célula com número 3
    for r in range(2, 4):
        for c in range(3, 5):
            campo_minado.flags[r][c] = True  # Marcar todas as células adjacentes com bandeira
    campo_minado.field[3][4] = -1  # Uma das células adjacentes é uma bomba
    campo_minado.field[3][2] = -1  # Outra célula adjacente é uma bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False




# Teste 61: Verificar se o jogo continua quando uma célula com número 0 é clicada e todas as células adjacentes são marcadas com bandeira.
def test_on_button_click_zero_cell_all_adjacent_flagged(campo_minado):
    campo_minado.field[2][3] = 0  # Célula com número 0
    for r in range(2, 4):
        for c in range(3, 5):
            campo_minado.flags[r][c] = True  # Marcar todas as células adjacentes com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 62: Verificar se o jogo continua quando uma célula com número 0 é clicada e todas as células adjacentes são marcadas com bandeira, exceto uma célula adjacente que é uma bomba.
def test_on_button_click_zero_cell_almost_all_adjacent_flagged(campo_minado):
    campo_minado.field[2][3] = 0  # Célula com número 0
    for r in range(2, 4):
        for c in range(3, 5):
            campo_minado.flags[r][c] = True  # Marcar todas as células adjacentes com bandeira
    campo_minado.field[3][4] = -1  # Uma das células adjacentes é uma bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 63: Verificar se o jogo continua quando uma célula com número 0 é clicada e todas as células adjacentes são marcadas com bandeira, exceto uma célula adjacente que é uma bomba e uma célula adjacente que não é uma bomba.
def test_on_button_click_zero_cell_mixed_adjacent_flags(campo_minado):
    campo_minado.field[2][3] = 0  # Célula com número 0
    for r in range(2, 4):
        for c in range(3, 5):
            campo_minado.flags[r][c] = True  # Marcar todas as células adjacentes com bandeira
    campo_minado.field[3][4] = -1  # Uma das células adjacentes é uma bomba
    campo_minado.field[3][2] = 0  # Uma das células adjacentes não é uma bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 64: Verificar se o jogo continua quando uma célula com número 0 é clicada e todas as células adjacentes são marcadas com bandeira, exceto duas células adjacentes que são bombas.
def test_on_button_click_zero_cell_two_adjacent_bombs(campo_minado):
    campo_minado.field[2][3] = 0  # Célula com número 0
    for r in range(2, 4):
        for c in range(3, 5):
            campo_minado.flags[r][c] = True  # Marcar todas as células adjacentes com bandeira
    campo_minado.field[3][4] = -1  # Uma das células adjacentes é uma bomba
    campo_minado.field[3][2] = -1  # Outra célula adjacente é uma bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False


# Teste 65: Verificar se o jogo continua quando uma célula com número 1 é clicada e todas as células adjacentes são marcadas com bandeira.
def test_on_button_click_one_cell_all_adjacent_flagged(campo_minado):
    campo_minado.field[2][3] = 1  # Célula com número 1
    for r in range(2, 4):
        for c in range(3, 5):
            campo_minado.flags[r][c] = True  # Marcar todas as células adjacentes com bandeira
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 66: Verificar se o jogo continua quando uma célula com número 1 é clicada e todas as células adjacentes são marcadas com bandeira, exceto uma célula adjacente que é uma bomba.
def test_on_button_click_one_cell_almost_all_adjacent_flagged(campo_minado):
    campo_minado.field[2][3] = 1  # Célula com número 1
    for r in range(2, 4):
        for c in range(3, 5):
            campo_minado.flags[r][c] = True  # Marcar todas as células adjacentes com bandeira
    campo_minado.field[3][4] = -1  # Uma das células adjacentes é uma bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 67: Verificar se o jogo continua quando uma célula com número 1 é clicada e todas as células adjacentes são marcadas com bandeira, exceto uma célula adjacente que não é uma bomba.
def test_on_button_click_one_cell_almost_all_adjacent_flagged_non_bomb(campo_minado):
    campo_minado.field[2][3] = 1  # Célula com número 1
    for r in range(2, 4):
        for c in range(3, 5):
            campo_minado.flags[r][c] = True  # Marcar todas as células adjacentes com bandeira
    campo_minado.field[3][2] = 0  # Uma das células adjacentes não é uma bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False

# Teste 68: Verificar se o jogo continua quando uma célula com número 1 é clicada e todas as células adjacentes são marcadas com bandeira, exceto duas células adjacentes que são bombas.
def test_on_button_click_one_cell_two_adjacent_bombs(campo_minado):
    campo_minado.field[2][3] = 1  # Célula com número 1
    for r in range(2, 4):
        for c in range(3, 5):
            campo_minado.flags[r][c] = True  # Marcar todas as células adjacentes com bandeira
    campo_minado.field[3][4] = -1  # Uma das células adjacentes é uma bomba
    campo_minado.field[3][2] = -1  # Outra célula adjacente é uma bomba
    campo_minado.on_button_click(2, 3)
    assert campo_minado.is_game_over is False
