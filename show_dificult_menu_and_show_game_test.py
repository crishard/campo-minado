import subprocess
import tkinter as tk
from campo_minado import create_game_instance, show_difficulty_menu, show_game, start_game
from functions.show_difficulty_menu import show_difficulty_menu_function
import pytest


@pytest.fixture
def root():
    return tk.Tk()

# Testa se o nível fácil é criado corretamente


def test_start_game_easy(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)
    current_difficulty = game.get_current_difficulty()
    assert current_difficulty == "Fácil"

# Testa se o nível intermediário é selecionado corretamente


def test_start_game_intermediate(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Intermediário", show_difficulty_menu_function, root)
    current_difficulty = game.get_current_difficulty()
    assert current_difficulty == "Intermediário"

# Testa se o nível difícil é selecionado corretamente


def test_start_game_hard(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Difícil", show_difficulty_menu_function, root)
    current_difficulty = game.get_current_difficulty()
    assert current_difficulty == "Difícil"


# Simula a criação da janela de escolha de nível
def test_choose_difficulty_window(root):
    show_difficulty_menu(root)

    assert len(root.winfo_children()) > 0
    assert isinstance(root.winfo_children()[0], tk.Frame)
    frame = root.winfo_children()[0]

    buttons = frame.winfo_children()

    assert any(button.winfo_class() == 'Button' for button in buttons)
