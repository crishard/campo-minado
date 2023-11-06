import tkinter as tk
from functions.show_difficulty_menu import show_difficulty_menu_function

def test_show_difficulty_menu_creation():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None) 
    children = root.winfo_children()
    frame = children[0]
    labels = frame.winfo_children()[0:2] 
    buttons = frame.winfo_children()[2:5]  
    assert len(buttons) == 3


def test_easy_button_creation():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None) 
    children = root.winfo_children()[0].winfo_children()[2] 
    if children.winfo_exists(): 
        assert children["text"] == "Fácil"

def test_intermediate_button_creation():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None)
    children = root.winfo_children()[0].winfo_children()[3]  # O índice 3 representa o botão "Intermediário"
    if children.winfo_exists():
        assert children["text"] == "Intermediário"


def test_hard_button_creation():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None)
    children = root.winfo_children()[0].winfo_children()[4]  # O índice 4 representa o botão "Difícil"
    if children.winfo_exists():
        assert children["text"] == "Difícil"

def test_options_menu_creation():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None)  # Passar função fictícia para show_game
    frame = root.winfo_children()[0]  # Pega o frame raiz
    options_buttons = frame.winfo_children()[7:10]  # Botões de opções

    for button in options_buttons:
        assert button.winfo_exists()  # Verifica se o botão está presente


def test_history_button_creation():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None) 
    children = root.winfo_children()[0].winfo_children()[5] 
    if children.winfo_exists(): 
        assert children["text"] == "Histórico"

def test_tutorial_button_creation():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None)
    children = root.winfo_children()[0].winfo_children()[6]  # O índice 3 representa o botão "Intermediário"
    if children.winfo_exists():
        assert children["text"] == "Tutorial"


def test_out_game_button_creation():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None)
    children = root.winfo_children()[0].winfo_children()[7]  # O índice 4 representa o botão "Difícil"
    if children.winfo_exists():
        assert children["text"] == "Sair do jogo"
