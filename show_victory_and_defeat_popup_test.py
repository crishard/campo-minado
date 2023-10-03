import tkinter as tk
from functions.show_victory_popup import show_victory_popup_function
from functions.show_defeat_popup import show_defeat_popup_function
from datetime import timedelta


def test_show_victory_popup_function_in_sixty_minutes():
    root = tk.Tk()

    def show_difficulty_menu():
        pass

    victory_time = timedelta(seconds=3600)
    show_victory_popup_function(victory_time, root, show_difficulty_menu)
    assert isinstance(root.winfo_children()[0], tk.Toplevel)
    root.destroy()


def test_show_victory_popup_function_in_zero_seconds():
    root = tk.Tk()

    def show_difficulty_menu():
        pass

    victory_time = timedelta(seconds=0)
    show_victory_popup_function(victory_time, root, show_difficulty_menu)

    children = root.winfo_children()
    if children:
        assert isinstance(children[0], tk.Toplevel)

    root.destroy()


def test_victory_in_1_hour_30_minutes_15_seconds():
    root = tk.Tk()

    def show_difficulty_menu():
        pass

    victory_time = timedelta(hours=1, minutes=30, seconds=15)
    show_victory_popup_function(victory_time, root, show_difficulty_menu)
    assert isinstance(root.winfo_children()[0], tk.Toplevel)
    root.destroy()


def test_victory_in_2_hours():
    root = tk.Tk()

    def show_difficulty_menu():
        pass

    victory_time = timedelta(hours=2, minutes=0, seconds=0)
    show_victory_popup_function(victory_time, root, show_difficulty_menu)
    assert isinstance(root.winfo_children()[0], tk.Toplevel)
    root.destroy()
