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
