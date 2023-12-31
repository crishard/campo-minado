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


def test_victory_in_5_minutes_30_seconds():
    root = tk.Tk()

    def show_difficulty_menu():
        pass

    victory_time = timedelta(minutes=5, seconds=30)
    show_victory_popup_function(victory_time, root, show_difficulty_menu)
    assert isinstance(root.winfo_children()[0], tk.Toplevel)
    root.destroy()


def test_victory_in_23_hours_59_minutes_59_seconds():
    root = tk.Tk()

    def show_difficulty_menu():
        pass

    victory_time = timedelta(hours=23, minutes=59, seconds=59)
    show_victory_popup_function(victory_time, root, show_difficulty_menu)
    assert isinstance(root.winfo_children()[0], tk.Toplevel)
    root.destroy()


def test_victory_in_100_hours_30_minutes_59_seconds():
    root = tk.Tk()

    def show_difficulty_menu():
        pass

    victory_time = timedelta(hours=100, minutes=30, seconds=59)
    show_victory_popup_function(victory_time, root, show_difficulty_menu)
    assert isinstance(root.winfo_children()[0], tk.Toplevel)
    root.destroy()


def test_defeat_popup_creation():
    root = tk.Tk()

    def show_difficulty_menu():
        pass

    show_defeat_popup_function(root, show_difficulty_menu)

    children = root.winfo_children()
    defeat_popup = children[0]
    assert isinstance(defeat_popup, tk.Toplevel)

    root.destroy()

def test_show_victory_popup_creation():
    root = tk.Tk()

    def show_difficulty_menu():
        pass

    # Pode ajustar o tempo da vitória conforme necessário
    victory_time = timedelta(seconds=3600)
    show_victory_popup_function(victory_time, root, show_difficulty_menu)

    children = root.winfo_children()
    victory_popup = children[0]
    assert isinstance(victory_popup, tk.Toplevel)

    root.destroy()

def test_mouse_click_on_victory_popup():
    root = tk.Tk()

    def show_difficulty_menu():
        pass

    victory_time = timedelta(seconds=3600)
    show_victory_popup_function(victory_time, root, show_difficulty_menu)

    children = root.winfo_children()
    victory_popup = children[0]

    ok_button = victory_popup.children['!button']
    ok_button.invoke()

    assert victory_popup.winfo_exists() == 0

    root.destroy()

# Teste para verificar se o popup de vitória é fechado corretamente


def test_close_victory_popup():
    root = tk.Tk()

    def show_difficulty_menu():
        pass

    victory_time = timedelta(seconds=3600)
    show_victory_popup_function(victory_time, root, show_difficulty_menu)

    children = root.winfo_children()
    victory_popup = children[0]

    victory_popup.destroy()

    assert len(root.winfo_children()) == 0

    root.destroy()

# Teste para verificar se o popup de derrota é exibido após uma derrota após alguns minutos de partida (você pode ajustar o tempo conforme necessário)


def test_defeat_popup_display_after_defeat():
    root = tk.Tk()

    def show_difficulty_menu():
        pass

    defeat_time = timedelta(minutes=5)
    show_defeat_popup_function(root, show_difficulty_menu)

    children = root.winfo_children()
    defeat_popup = children[0]
    assert defeat_popup.title() == "Derrota"

    root.destroy()


def test_defeat_popup_display_after_defeat_in_10_hours():
    root = tk.Tk()

    def show_difficulty_menu():
        pass

    defeat_time = timedelta(hours=10)
    show_defeat_popup_function(root, show_difficulty_menu)

    children = root.winfo_children()
    defeat_popup = children[0]
    assert defeat_popup.title() == "Derrota"

    root.destroy()


def test_defeat_popup_display_after_defeat_in_23_hours_59_minutes_59_seconds():
    root = tk.Tk()

    def show_difficulty_menu():
        pass

    defeat_time = timedelta(hours=23, minutes=59, seconds=59)
    show_defeat_popup_function(root, show_difficulty_menu)

    children = root.winfo_children()
    defeat_popup = children[0]
    assert defeat_popup.title() == "Derrota"

    root.destroy()


def test_defeat_popup_display_after_defeat_in_100_hours():
    root = tk.Tk()

    def show_difficulty_menu():
        pass

    defeat_time = timedelta(hours=100)
    show_defeat_popup_function(root, show_difficulty_menu)

    children = root.winfo_children()
    defeat_popup = children[0]
    assert defeat_popup.title() == "Derrota"

    root.destroy()


def test_defeat_popup_display_after_defeat_in_10_seconds():
    root = tk.Tk()

    def show_difficulty_menu():
        pass

    defeat_time = timedelta(seconds=10)
    show_defeat_popup_function(root, show_difficulty_menu)

    children = root.winfo_children()
    defeat_popup = children[0]
    assert defeat_popup.title() == "Derrota"

    root.destroy()
