import pytest
import tkinter as tk
from campo_minado import create_game_instance

def test_no_game_saved_to_history_after_end_game():
   
    root = tk.Tk()
    game = create_game_instance(root, 8, 8, 10)
    
    historico_anterior = game.historico_partidas.copy()
    
    game.end_game()
    
    assert game.historico_partidas == historico_anterior

def test_no_game_saved_to_history_after_game_over():
   
    root = tk.Tk()
    game = create_game_instance(root, 8, 8, 10)
    
    game.game_over = True
    
    assert game.historico_partidas


def test_no_game_saved_to_history_after_victory():
   
    root = tk.Tk()
    game = create_game_instance(root, 8, 8, 10)
    historico_anterior = game.historico_partidas.copy()
    game.show_victory_popup
    
    assert game.historico_partidas == historico_anterior
