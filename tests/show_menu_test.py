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
