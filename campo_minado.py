import tkinter as tk
import random
import datetime

class CampoMinado:
    def __init__(self, root, rows, cols, bombs, show_difficulty_menu):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.field = [[0 for _ in range(cols)] for _ in range(rows)]
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.flags = [[False for _ in range(cols)] for _ in range(rows)]
        self.started = False
        self.show_difficulty_menu = show_difficulty_menu
        self.game_over = False
        self.is_game_over = False
        self.pause_button_enabled = True
        self.start_time = None
        self.pause_start_time = None
        self.paused = False
        self.pause_button = None
        self.bomb_count = 0
        self.pause_label = None
        self.victory_time = None
        self.create_widgets()
        self.place_bombs()
        self.calculate_numbers()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=1, column=1, padx=10, pady=10)

        self.pause_button = tk.Button(
            self.frame, text='Pausar', command=self.toggle_pause)
        self.pause_button.grid(
            row=self.rows + 2, columnspan=self.cols + 1, pady=5)
        self.pause_label = tk.Label(self.frame, text='')
        self.pause_label.grid(
            row=self.rows + 3, columnspan=self.cols + 1, pady=5)

        for row in range(self.rows):
            letter_label = tk.Label(self.frame, text=chr(65 + row))
            letter_label.grid(row=row + 1, column=0, padx=3)

        for col in range(self.cols):
            number_label = tk.Label(self.frame, text=str(col + 1), pady=2)
            number_label.grid(row=0, column=col + 1)

        for row in range(self.rows):
            for col in range(self.cols):
                button = tk.Button(self.frame, text='', command=lambda r=row,
                                   c=col: self.on_button_click(r, c), width=2)
                button.grid(row=row + 1, column=col + 1)
                self.buttons[row][col] = button
                button.bind("<Button-3>", lambda event, r=row,
                            c=col: self.on_right_click(event, r, c))

        self.time_label = tk.Label(self.frame, text="Tempo: 0")
        self.time_label.grid(
            row=self.rows + 1, columnspan=self.cols + 1, pady=8)

    def place_bombs(self):
        bomb_count = 0
        while bomb_count < self.bombs:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if self.field[row][col] == 0:
                self.field[row][col] = -1
                bomb_count += 1

    def toggle_pause(self):
        if self.pause_button_enabled: 
                
            if not self.game_over:  # Verifique se o jogo ainda está em andamento
                self.paused = not self.paused
                if self.paused:
                    self.pause_button.config(text='Retomar')
                    self.pause_label.config(
                        text='Você precisa retomar o jogo para realizar alguma ação.')
                    self.pause_start_time = datetime.datetime.now()
                else:
                    self.pause_button.config(text='Pausar')
                    self.pause_label.config(text='')
                    if self.started:
                        self.current_time = datetime.datetime.now()
                        self.start_time += self.current_time - self.pause_start_time
                        self.update_time()
        else:
            self.pause_label.config(text='O jogo acabou.')  # Exiba uma mensagem quando o jogo acabar
   

    def update_time(self):
        if self.started and not self.game_over and not self.is_game_over and not self.paused:
            elapsed_time = datetime.datetime.now() - self.start_time
            self.victory_time = elapsed_time
            elapsed_time_str = str(elapsed_time).split('.')[0]
            self.time_label.config(text=f"Tempo: {elapsed_time_str}")
            self.root.after(1000, self.update_time)

    def show_defeat_popup(self):
        defeat_popup = tk.Toplevel(self.root, padx=10, pady=10)
        defeat_popup.title("Derrota")
        defeat_message = "Você perdeu o jogo. Tente novamente!"
        defeat_label = tk.Label(defeat_popup, text=defeat_message, padx=20, pady=20)
        defeat_label.pack()
        
        def return_to_menu():
            defeat_popup.destroy()  # Feche a janela de derrota
            for widget in self.root.winfo_children():
                widget.destroy()
            self.show_difficulty_menu()
        
        ok_button = tk.Button(defeat_popup, text="Voltar ao menu", command=return_to_menu)
        ok_button.pack()


    def show_victory_popup(self):
        if self.victory_time:

            hours, remainder = divmod(self.victory_time.total_seconds(), 3600)
            minutes, seconds = divmod(remainder, 60)
            victory_message = f"Parabéns! Você venceu em {int(hours)} horas, {int(minutes)} minutos e {int(seconds)} segundos! 🎉🏆"

            def return_to_menu():
                for widget in self.root.winfo_children():
                    widget.destroy()
                self.show_difficulty_menu()

            victory_popup = tk.Toplevel(self.root, padx=10, pady=10)
            victory_popup.title("Vitória")
            victory_label = tk.Label(
                victory_popup, text=victory_message, padx=20, pady=20)
            victory_label.pack()
            ok_button = tk.Button(victory_popup, text="OK",
                                  command=return_to_menu)
            ok_button.pack()

    def check_game_over(self):
        if all(self.field[row][col] == -1 or self.flags[row][col] for row in range(self.rows) for col in range(self.cols)):
            self.game_over = True
            self.victory_time = datetime.datetime.now() - self.start_time
            self.show_victory_popup()

    def reveal_all_bombs(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.field[row][col] == -1:
                    self.buttons[row][col].config(text='💣')

    def end_game(self):
        self.game_over = True
        self.time_label.config(text="Você perdeu!")
        self.reveal_all_bombs()
        self.pause_button_enabled = False  # Bloqueie o botão "Pausar"
        self.show_defeat_popup()  # Chame a função para exibir a mensagem de derrota

    def calculate_numbers(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.field[row][col] == -1:
                    continue
                bomb_count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if 0 <= row + dr < self.rows and 0 <= col + dc < self.cols:
                            if self.field[row + dr][col + dc] == -1:
                                bomb_count += 1
                self.field[row][col] = bomb_count

    def on_right_click(self, event, row, col):
        if self.game_over or self.flags[row][col] or self.paused:
            return

        if self.buttons[row][col]['text'] == '':
            if not self.flags[row][col] and self.bomb_count < self.bombs:
                self.buttons[row][col].config(text='🏳')
                self.flags[row][col] = True
                self.bomb_count += 1
        elif self.buttons[row][col]['text'] == '🏳':
            self.buttons[row][col].config(text='')
            self.flags[row][col] = False
            self.bomb_count -= 1

    def on_button_click(self, row, col):
        if self.game_over or self.is_game_over or self.flags[row][col] or self.paused:
            return

        if not self.started:
            self.started = True
            self.start_time = datetime.datetime.now()  # Inicialize o tempo de início aqui
            self.update_time()

        if self.is_game_over or self.flags[row][col]:
            return

        if self.field[row][col] == -1:
            self.end_game()
        else:
            bomb_count = self.field[row][col]
            self.buttons[row][col].config(text=str(bomb_count))
            self.flags[row][col] = True

        self.check_game_over()


def start_game(rows, cols, bombs, root, show_difficulty_menu):
    for widget in root.winfo_children():
        widget.destroy()

    game = CampoMinado(root, rows, cols, bombs, show_difficulty_menu)


def main():
    root = tk.Tk()
    root.title("Campo Minado")

    def show_difficulty_menu():
        for widget in root.winfo_children():
            widget.destroy()

        frame = tk.Frame(root)
        frame.grid(row=0, column=0, padx=10, pady=10)

        label = tk.Label(frame, text="Escolha o nível de dificuldade:")
        label2 = tk.Label(frame, text="Mais acoes dentro do jogo")
        label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        label2.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        def show_history():
            # Implemente a lógica para exibir o histórico de jogos anteriores na mesma tela
            pass

        def show_tutorial():
            # Crie uma nova janela para o tutorial
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
        # Limpe a tela atual
            for widget in root.winfo_children():
                widget.destroy()

            tutorial_label = tk.Label(
                root, text=tutorial_text, font=("Helvetica", 14), justify="left", padx=20, pady=20)
            tutorial_label.pack()

            # Adicione um botão "Voltar" para retornar à tela de menu principal
            back_button = tk.Button(
                root, text="Voltar ao Menu", command=show_difficulty_menu, pady=10)
            back_button.pack()

        def close_game():
            root.destroy()

        def start_game_button(difficulty):
            show_game(difficulty, show_difficulty_menu)

        easy_button = tk.Button(frame, text="Fácil",
                                command=lambda: start_game_button("Fácil"))
        intermediate_button = tk.Button(
            frame, text="Intermediário", command=lambda: start_game_button("Intermediário"))
        hard_button = tk.Button(frame, text="Difícil",
                                command=lambda: start_game_button("Difícil"))

        easy_button.grid(row=1, column=0, padx=10, pady=10)
        intermediate_button.grid(row=1, column=1, padx=10, pady=10)
        hard_button.grid(row=1, column=2, padx=10, pady=10)
        # Adicione um botão de histórico
        history_button = tk.Button(
            frame, text='Histórico', command=show_history)
        history_button.grid(row=3, column=0, padx=10, pady=10)

        # Adicione um botão de tutorial
        tutorial_button = tk.Button(
            frame, text='Tutorial', command=show_tutorial)
        tutorial_button.grid(row=3, column=1, padx=10, pady=10)
        # Adicione um botão de tutorial
        close_game_button = tk.Button(
            frame, text='Sair do jogo', command=close_game)
        close_game_button.grid(row=3, column=2, padx=10, pady=10)

    def show_game(difficulty, show_difficulty_menu):
        if difficulty == "Fácil":
            start_game(8, 8, 1, root, show_difficulty_menu)
        elif difficulty == "Intermediário":
            start_game(10, 16, 30, root, show_difficulty_menu)
        elif difficulty == "Difícil":
            start_game(24, 24, 100, root, show_difficulty_menu)

    show_difficulty_menu()

    root.mainloop()


if __name__ == "__main__":
    main()
