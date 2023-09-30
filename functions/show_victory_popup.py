import tkinter as tk


def show_victory_popup_function(victory_time, root, show_difficulty_menu):
    if victory_time:

        hours, remainder = divmod(victory_time.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)
        victory_message = f"Parabéns! Você venceu em {int(hours)} horas, {int(minutes)} minutos e {int(seconds)} segundos! 🎉🏆"

        def return_to_menu():
            for widget in root.winfo_children():
                widget.destroy()
            show_difficulty_menu()

        victory_popup = tk.Toplevel(root, padx=10, pady=10)
        victory_popup.title("Vitória")
        victory_label = tk.Label(
            victory_popup, text=victory_message, padx=20, pady=20)
        victory_label.pack()
        ok_button = tk.Button(victory_popup, text="OK",
                              command=return_to_menu)
        ok_button.pack()
