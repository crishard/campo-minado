import tkinter as tk


def show_tutorial_function(root, show_difficulty_menu_function, show_game):

    def show_difficulty_menu():
        show_difficulty_menu_function(root, show_game)

    tutorial_text = """
    Tutorial do Campo Minado:

    Regras do Jogo:

    1. O objetivo do jogo é abrir todos os campos sem bombas.
    2. Cada campo aberto mostrará um número, indicando quantas bombas estão adjacentes a ele.
    3. Use a lógica para determinar onde as bombas estão e evite clicar nelas.
    4. Use botões direito para marcar campos suspeitos com bandeiras.
    5. Marque todas as bombas para vencer o jogo.

    Boa sorte e divirta-se jogando!
    """
    for widget in root.winfo_children():
        widget.destroy()

    tutorial_label = tk.Label(
        root, text=tutorial_text, font=("Helvetica", 14), justify="left", padx=20, pady=20)
    tutorial_label.pack()

    back_button = tk.Button(
        root, text="Voltar ao Menu", command=show_difficulty_menu, pady=10)
    back_button.pack(side=tk.BOTTOM, pady=10)