import pytest
import datetime
from tkinter import Tk
from campo_minado import CampoMinado 

@pytest.fixture
def campo_minado():
    root = Tk()
    return CampoMinado(root, 8, 8, 1, lambda: None)

def test_update_time(campo_minado):
    campo_minado.started = True
    campo_minado.start_time = datetime.datetime.now()
    campo_minado.update_time()
    elapsed_time = campo_minado.time_label.cget('text')
    assert "Tempo: 0:00:00" in elapsed_time


def test_update_time_paused(campo_minado):
    campo_minado.started = True
    campo_minado.start_time = datetime.datetime(2023, 1, 1, 0, 0, 0)
    campo_minado.paused = True
    campo_minado.update_time()
    elapsed_time = campo_minado.time_label.cget('text')
    assert elapsed_time == "Tempo: 0"  


def test_update_time_game_over(campo_minado):
    campo_minado.started = True
    campo_minado.start_time = datetime.datetime(2023, 1, 1, 0, 0, 0)
    campo_minado.game_over = True
    campo_minado.update_time()
    elapsed_time = campo_minado.time_label.cget('text')
    assert elapsed_time == "Tempo: 0"   # Verifique se a string atualizada está vazia


def test_update_time_victory(campo_minado):
    campo_minado.started = True
    campo_minado.start_time = datetime.datetime(2023, 1, 1, 0, 0, 0)
    campo_minado.is_game_over = True
    campo_minado.paused = False
    campo_minado.update_time()
    elapsed_time = campo_minado.time_label.cget('text')
    assert elapsed_time == "Tempo: 0" 

def test_toggle_pause(campo_minado):
    campo_minado.toggle_pause()
    campo_minado.toggle_pause()
    assert campo_minado.paused is False

def test_toggle_pause_after_start(campo_minado):
    campo_minado.started = True
    campo_minado.start_time = datetime.datetime.now()
    campo_minado.toggle_pause()
    campo_minado.toggle_pause()
    assert campo_minado.paused is False

def test_end_game(campo_minado):
    campo_minado.end_game()
    assert campo_minado.bomb_count == -2 

#  Testar se a partida e inciada se o time for iniciado manualmente
def test_time_manual_init():
    campo_minado.started = False
    campo_minado.start_time = datetime.datetime.now()

    assert campo_minado.started is False

