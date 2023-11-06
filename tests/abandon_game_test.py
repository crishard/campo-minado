import datetime
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
    campo_minado.abandon_game()

    assert campo_minado.game_over is not True

def test_abandon_game_paused(campo_minado, mocker):
    mocker.patch.object(campo_minado, 'show_difficulty_menu', return_value=None)
    campo_minado.paused = True
    campo_minado.abandon_game()

    assert campo_minado.game_over is not  True

def test_abandon_game_after_long_time(campo_minado, mocker):
    campo_minado.start_time = campo_minado.pause_start_time = mocker.Mock()
    campo_minado.start_time = datetime.datetime.now() - datetime.timedelta(hours=10)
    campo_minado.abandon_game()

    assert campo_minado.game_over is not True


def test_abandon_game_game_not_started(campo_minado, mocker):
    campo_minado.start_time = campo_minado.pause_start_time = mocker.Mock()
    campo_minado.started = False
    campo_minado.abandon_game()

    assert campo_minado.game_over is not True


def test_abandon_game_create(campo_minado, mocker):
    campo_minado.start_time = campo_minado.pause_start_time = mocker.Mock()
    campo_minado.abandon_game()

    assert campo_minado.game_over is not True