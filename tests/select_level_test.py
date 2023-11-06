import tkinter as tk
from campo_minado import start_game
from functions.show_difficulty_menu import show_difficulty_menu_function

# testes do nivel facil
def test_easy_button_visibility():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None) 
    frame = root.winfo_children()[0]  
    easy_button = frame.winfo_children()[2]  
    visible_button = easy_button.winfo_viewable
    assert visible_button != False

def test_easy_button_clickable():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None) 
    frame = root.winfo_children()[0]
    easy_button = frame.winfo_children()[2] 
    button_class = easy_button.winfo_class()

    assert button_class == "Button"

def test_button_comportment():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None) 
    frame = root.winfo_children()[0]
    easy_button = frame.winfo_children()[2] 
    created_game = None

    def fake_start_game(rows, cols, bombs, root, show_difficulty_menu):
        nonlocal created_game
        created_game = start_game(rows, cols, bombs, root, show_difficulty_menu)

    easy_button.config(command=lambda: fake_start_game(8, 8, 1, root, show_difficulty_menu_function))
    easy_button.invoke() 

    assert created_game is not None

def test_menu_cleanup_after_click():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None)  
    frame = root.winfo_children()[0] 
    easy_button = frame.winfo_children()[2] 
    easy_button.invoke()

    assert len(root.winfo_children()) == 1


def test_start_game_creation():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None) 
    frame = root.winfo_children()[0]
    easy_button = frame.winfo_children()[2] 
    created_game = None

    def fake_start_game(rows, cols, bombs, root, show_difficulty_menu):
        nonlocal created_game
        created_game = start_game(rows, cols, bombs, root, show_difficulty_menu)

    easy_button.config(command=lambda: fake_start_game(8, 8, 10, root, show_difficulty_menu_function))
    easy_button.invoke() 
    rows = created_game.rows
    cols = created_game.cols
    bombs = created_game.bombs

    assert rows and cols and bombs is not False


# testes do nivel intermediario
def test_intermediate_button_visibility():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None) 
    frame = root.winfo_children()[0]  
    intermediate_button = frame.winfo_children()[3]  
    visible_button = intermediate_button.winfo_viewable
    assert visible_button != False

def test_intermediate_button_clickable():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None) 
    frame = root.winfo_children()[0]
    intermediate_button = frame.winfo_children()[3] 
    button_class = intermediate_button.winfo_class()

    assert button_class == "Button"

def test_button_intermediate_comportment():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None) 
    frame = root.winfo_children()[0]
    intermediate_button = frame.winfo_children()[3] 
    created_game = None

    def fake_start_game(rows, cols, bombs, root, show_difficulty_menu):
        nonlocal created_game
        created_game = start_game(rows, cols, bombs, root, show_difficulty_menu)

    intermediate_button.config(command=lambda: fake_start_game(10, 16, 30, root, show_difficulty_menu_function))
    intermediate_button.invoke() 

    assert created_game is not None

def test_menu_cleanup_after_click_intermediate():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None)  
    frame = root.winfo_children()[0] 
    intermediate_button = frame.winfo_children()[3] 
    intermediate_button.invoke()

    assert len(root.winfo_children()) == 1


def test_start_game_creation_intermediate():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None) 
    frame = root.winfo_children()[0]
    intermediate_button = frame.winfo_children()[3] 
    created_game = None

    def fake_start_game(rows, cols, bombs, root, show_difficulty_menu):
        nonlocal created_game
        created_game = start_game(rows, cols, bombs, root, show_difficulty_menu)

    intermediate_button.config(command=lambda: fake_start_game(8, 8, 1, root, show_difficulty_menu_function))
    intermediate_button.invoke() 
    rows = created_game.rows
    cols = created_game.cols
    bombs = created_game.bombs

    assert rows and cols and bombs is not False

# testes do nivel dificil

def test_hard_button_visibility():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None) 
    frame = root.winfo_children()[0]  
    hard_button = frame.winfo_children()[4]  
    visible_button = hard_button.winfo_viewable
    assert visible_button != False

def test_hard_button_clickable():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None) 
    frame = root.winfo_children()[0]
    hard_button = frame.winfo_children()[4] 
    button_class = hard_button.winfo_class()

    assert button_class == "Button"

def test_button_hard_comportment():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None) 
    frame = root.winfo_children()[0]
    hard_button = frame.winfo_children()[4] 
    created_game = None

    def fake_start_game(rows, cols, bombs, root, show_difficulty_menu):
        nonlocal created_game
        created_game = start_game(rows, cols, bombs, root, show_difficulty_menu)

    hard_button.config(command=lambda: fake_start_game(24, 24, 100, root, show_difficulty_menu_function))
    hard_button.invoke() 

    assert created_game is not None

def test_menu_cleanup_after_click_hard():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None)  
    frame = root.winfo_children()[0] 
    hard_button = frame.winfo_children()[4] 
    hard_button.invoke()

    assert len(root.winfo_children()) == 1


def test_start_game_creation_hard():
    root = tk.Tk()
    show_difficulty_menu_function(root, lambda x, y: None) 
    frame = root.winfo_children()[0]
    hard_button = frame.winfo_children()[4] 
    created_game = None

    def fake_start_game(rows, cols, bombs, root, show_difficulty_menu):
        nonlocal created_game
        created_game = start_game(rows, cols, bombs, root, show_difficulty_menu)

    hard_button.config(command=lambda: fake_start_game(8, 8, 1, root, show_difficulty_menu_function))
    hard_button.invoke() 
    rows = created_game.rows
    cols = created_game.cols
    bombs = created_game.bombs

    assert rows and cols and bombs is not False