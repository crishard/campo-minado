import tkinter as tk
import random
import time

class CampoMinado:
    def __init__(self, root, rows, cols, bombs):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.field = [[0 for _ in range(cols)] for _ in range(rows)]
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.flags = [[False for _ in range(cols)] for _ in range(rows)]
        self.started = False
        self.game_over = False
        self.is_game_over = False
        self.start_time = None
        self.paused = False
        self.pause_button = None
        self.bomb_count = 0
        self.pause_label = None
        self.create_widgets()
        self.place_bombs()
        self.calculate_numbers()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=1, column=1, padx=10, pady=10)

        self.pause_button = tk.Button(self.frame, text='Pausar', command=self.toggle_pause)
        self.pause_button.grid(row=self.rows + 2, columnspan=self.cols + 1, pady=5)
        self.pause_label = tk.Label(self.frame, text='')
        self.pause_label.grid(row=self.rows + 3, columnspan=self.cols + 1, pady=5)

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
        self.paused = not self.paused
        if self.paused:
            self.pause_button.config(text='Retomar')
            self.pause_label.config(text='Você precisa retomar o jogo para realizar alguma ação.')
        else:
            self.pause_button.config(text='Pausar')
            self.pause_label.config(text='')
            if self.started:
                self.start_time = time.time() - (self.current_time - self.start_time)
                self.update_time()


    def update_time(self):
        if self.started and not self.game_over and not self.is_game_over and not self.paused:
            self.current_time = time.time()  # Registre o tempo atual.
            elapsed_time = int((self.current_time - self.start_time))
            self.time_label.config(text=f"Tempo: {elapsed_time}")
            self.root.after(1000, self.update_time)

    def check_game_over(self):
        if all(self.field[row][col] == -1 or self.flags[row][col] for row in range(self.rows) for col in range(self.cols)):
            self.game_over = True
            self.time_label.config(text="Você venceu!")

    def reveal_all_bombs(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.field[row][col] == -1:
                    self.buttons[row][col].config(text='💣')

    def end_game(self):
        self.game_over = True
        self.time_label.config(text="Você perdeu!")
        self.reveal_all_bombs()

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
            self.start_time = time.time()
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


def start_game(rows, cols, bombs, root):
    for widget in root.winfo_children():
        widget.destroy()

    game = CampoMinado(root, rows, cols, bombs)


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
            # Implemente a lógica para exibir um tutorial sobre como jogar o Campo Minado na mesma tela
            pass

        def close_game():
            root.destroy()

        def start_game_button(difficulty):
            show_game(difficulty)

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
        history_button = tk.Button(frame, text='Histórico', command=show_history)
        history_button.grid(row=3, column=0, padx=10, pady=10)

        # Adicione um botão de tutorial
        tutorial_button = tk.Button(frame, text='Tutorial', command=show_tutorial)
        tutorial_button.grid(row=3, column=1, padx=10, pady=10)
           # Adicione um botão de tutorial
        close_game_button = tk.Button(frame, text='Sair do jogo', command=close_game)
        close_game_button.grid(row=3, column=2, padx=10, pady=10)

        

    def show_game(difficulty):
        if difficulty == "Fácil":
            start_game(8, 8, 1, root)
        elif difficulty == "Intermediário":
            start_game(10, 16, 30, root)
        elif difficulty == "Difícil":
            start_game(24, 24, 100, root)

    show_difficulty_menu()

    root.mainloop()


if __name__ == "__main__":
    main()
