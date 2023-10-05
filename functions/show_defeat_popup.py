import tkinter as tk
from functions.show_difficulty_menu import show_difficulty_menu_function

def show_defeat_popup_function(root, show_game):
        defeat_popup = tk.Toplevel(root, padx=10, pady=10)
        defeat_popup.title("Derrota")
        defeat_message = "Você perdeu o jogo. Tente novamente!"
        defeat_label = tk.Label(
            defeat_popup, text=defeat_message, padx=20, pady=20)
        defeat_label.pack()

        def return_to_menu():
            defeat_popup.destroy()
            for widget in root.winfo_children():
                widget.destroy()
            show_difficulty_menu_function(root, show_game)

        ok_button = tk.Button(
            defeat_popup, text="Voltar ao menu", command=return_to_menu)
        ok_button.pack()