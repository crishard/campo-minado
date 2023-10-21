import subprocess
import tkinter as tk
from campo_minado import create_game_instance, show_difficulty_menu, show_game, start_game, CampoMinado
from functions.show_difficulty_menu import show_difficulty_menu_function
import pytest



@pytest.fixture
def root():
    return tk.Tk()


def test_is_not_level_defined(root): 
    show_difficulty_menu_function(root, show_game)
    try:
        game = show_game("dsds", show_difficulty_menu_function, root)
        game.current_difficulty()
    except Exception as e:
        assert str(e) == "'NoneType' object has no attribute 'current_difficulty'"

# Testa se o nível fácil é criado corretamente

def test_board_is_covered(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    # Define um valor padrão para células vazias (por exemplo, 0)
    default_value = ''

    # Verifica se todas as células do tabuleiro têm valores diferentes do valor padrão
    for row in range(game.rows):
        for col in range(game.cols):
            cell_value = game.field[row][col]
            assert cell_value != default_value, f"Célula ({row}, {col}) não foi gerada"


def test_board_generated(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    # Define um valor padrão para células vazias (por exemplo, 0)
    default_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, -1]

    # Verifica se todas as células do tabuleiro têm valores diferentes do valor padrão
    for row in range(game.rows):
        for col in range(game.cols):
            cell_value = game.field[row][col]
            assert cell_value != default_value, f"Célula ({row}, {col}) não foi gerada"


def test_no_zone_has_flags(root):
    show_difficulty_menu_function(root, show_game)
    game = show_game("Fácil", show_difficulty_menu_function, root)

    # Verifica se nenhuma zona do tabuleiro tem bandeira
    for row in range(game.rows):
        for col in range(game.cols):
            if game.field[row][col] != -1 and game.flags[row][col]:
                assert False, f"Célula ({row}, {col}) tem uma bandeira em uma zona sem bomba"



def test_bomb_distribution(root):
    # Número de vezes que o teste será executado
    num_tests = 100
    bomb_counts = None  # Inicialize bomb_counts como None

    for _ in range(num_tests):
        show_difficulty_menu_function(root, show_game)
        game = show_game("Fácil", show_difficulty_menu_function, root)

        if bomb_counts is None:
            # Inicialize bomb_counts na primeira iteração
            bomb_counts = [[0 for _ in range(game.cols)] for _ in range(game.rows)]

        for row in range(game.rows):
            for col in range(game.cols):
                if game.field[row][col] == -1:
                    bomb_counts[row][col] += 1

    # Verifique se a distribuição das bombas é razoavelmente uniforme
    threshold = num_tests // game.rows // game.cols // 2  # Aproximadamente metade das células
    for row in range(game.rows):
        for col in range(game.cols):
            assert bomb_counts[row][col] >= threshold, f"Distribuição de bombas não é aleatória em ({row}, {col})"
