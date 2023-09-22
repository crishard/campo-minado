import tkinter as tk
import random

class CampoMinado:
    def __init__(self, root, rows, cols, bombs):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.field = [[0 for _ in range(cols)] for _ in range(rows)]
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.create_widgets()
        self.place_bombs()
        self.calculate_numbers()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        for row in range(self.rows):
            for col in range(self.cols):
                button = tk.Button(self.frame, width=2, height=1, command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def place_bombs(self):
        bomb_count = 0
        while bomb_count < self.bombs:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if self.field[row][col] == 0:
                self.field[row][col] = -1
                bomb_count += 1

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

    def on_button_click(self, row, col):
        if self.field[row][col] == -1:
            self.buttons[row][col].config(text="X", state="disabled")
            self.game_over()
        else:
            self.buttons[row][col].config(text=str(self.field[row][col]), state="disabled")

    def game_over(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.field[row][col] == -1:
                    self.buttons[row][col].config(text="X", state="disabled")

def start_game(rows, cols, bombs):
    root = tk.Tk()
    root.title("Campo Minado")
    game = CampoMinado(root, rows, cols, bombs)
    root.mainloop()

def main():
    print("Escolha o nível de dificuldade:")
    print("1 - Fácil (8x8 com 10 bombas)")
    print("2 - Intermediário (10x16 com 30 bombas)")
    print("3 - Difícil (24x24 com 100 bombas)")
    
    choice = input("Digite o número do nível: ")
    
    if choice == "1":
        start_game(8, 8, 10)
    elif choice == "2":
        start_game(10, 16, 30)
    elif choice == "3":
        start_game(24, 24, 100)
    else:
        print("Escolha inválida. Por favor, escolha um nível válido.")

if __name__ == "__main__":
    main()
