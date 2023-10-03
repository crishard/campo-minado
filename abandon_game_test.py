import pytest
from tkinter import Tk
from campo_minado import CampoMinado

@pytest.fixture
def campo_minado():
    root = Tk()
    root.withdraw()
    game = CampoMinado(root, 8, 8, 1, None)
    yield game
    root.quit()


def test_abandon_game_game_over(campo_minado, mocker):
    mocker.patch.object(campo_minado, 'show_difficulty_menu', return_value=None)
    campo_minado.game_over = True
    campo_minado.abandon_game()
    mocker.patch.object(campo_minado, 'show_difficulty_menu', side_effect=pytest.fail)
    campo_minado.abandon_game()

def test_toggle_pause_paused(campo_minado):
    campo_minado.paused = True
    campo_minado.toggle_pause()
    assert not campo_minado.paused
    assert campo_minado.pause_button.cget('text') == 'Pausar'
    assert campo_minado.pause_label.cget('text') == ''

def test_toggle_pause_not_paused(campo_minado, mocker):
    campo_minado.start_time = campo_minado.pause_start_time = mocker.Mock()
    campo_minado.paused = False
    campo_minado.toggle_pause()
    assert campo_minado.paused
    assert campo_minado.pause_button.cget('text') == 'Retomar'
    assert campo_minado.pause_label.cget('text') == 'Você precisa retomar o jogo para realizar alguma ação.'
