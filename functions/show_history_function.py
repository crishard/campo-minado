import json
import tkinter as tk
from tkinter import ttk

def display_history(root, show_difficulty_menu_function, show_game):
    def show_difficulty_menu():
        show_difficulty_menu_function(root, show_game)

    historico_partidas = load_historico_partidas()
    for widget in root.winfo_children():
        widget.destroy()

    if not historico_partidas:
        no_data_label = tk.Label(root, text="Nenhuma partida registrada no histórico.")
        no_data_label.pack()
        back_button = tk.Button(
        root, text="Voltar ao Menu", command=show_difficulty_menu, pady=10)
        back_button.pack(side=tk.BOTTOM, pady=10)
    else:
        tree = ttk.Treeview(root, columns=("id","Difficulty", "Result", "Time Elapsed"), show="headings")
        tree.heading("id", text="id")
        tree.heading("Difficulty", text="Dificuldade")
        tree.heading("Result", text="Resultado")
        tree.heading("Time Elapsed", text="Tempo")
        id = 0
        for partida in historico_partidas:
            id = id
            difficulty = partida['difficulty']
            result = partida['result']
            time_elapsed = partida['time_elapsed']
            tree.insert("", "end", values=(id, difficulty, result, time_elapsed))
            id+=1
        tree.grid(row=1, column=0, padx=10, pady=10)


    back_button = tk.Button(root, text="Voltar ao Menu", command=show_difficulty_menu, pady=10)
    back_button.grid(row=2, column=0, padx=10, pady=10)



def load_historico_partidas():
    try:
        with open('historico_partidas.json', 'r') as json_file:
            data = json_file.read()
            if data:
                return json.loads(data)
            else:
                return []
    except FileNotFoundError:
        # Se o arquivo não existe, comece com uma lista vazia
        return []
    except json.decoder.JSONDecodeError:
        # Se o arquivo existe, mas não é um JSON válido, comece com uma lista vazia
        return []