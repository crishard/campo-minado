import pytest
from campo_minado import CampoMinado


# Teste para todas as celuas adjacentes serem bombas
def test_reveal_cell_all_adjacent_cells_bombs():
    game = CampoMinado(root=None, rows=8, cols=8,
                       bombs=10, show_difficulty_menu=None)
    game.field = [
        [-1, -1, -1,  0,  0,  0,  0,  0],
        [-1,  0, -1,  0, 0, -1, -1,  0],
        [-1, -1,  -1,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0, -1,  0],
        [0, -1,  0,  0,  0,  0,  0,  0],
        [0, -1,  0,  0,  0, -1, -1, -1],
        [0,  0,  0, -1,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0]
    ]
    game.reveal_cell(1, 1)
    assert game.flags == [
        [False, False, False,  False,  False,  False,  False,  False],
        [False,  True, False,  False, False, False, False,  False],
        [False, False,  False,  False,  False,  False,  False,  False],
        [False,  False,  False,  False,  False,  False, False,  False],
        [False, False,  False,  False,  False,  False,  False,  False],
        [False, False,  False,  False,  False, False, False, False],
        [False,  False,  False, False,  False,  False,  False,  False],
        [False,  False,  False,  False,  False,  False,  False,  False]
    ]

def test_reveal_cell_reveals_zero_neighboring_cells():
    game = CampoMinado(root=None, rows=3, cols=3,
                       bombs=1, show_difficulty_menu=None)
    game.field = [
        [0, 0, 0],
        [0, -1, 0],
        [0, 0, 0]
    ]
    game.reveal_cell(1, 1)  # a célula contem bomba, jogo encerrado
    assert game.flags == [
        [False, False, False],
        [False, False, False],
        [False, False, False]
    ]


def test_reveal_cell_reveals_neighboring_cells_with_numbers():
    game = CampoMinado(root=None, rows=3, cols=3,
                       bombs=0, show_difficulty_menu=None)
    game.field = [
        [1, 1, 1],
        [1, -1, 1],
        [1, 1, 1]
    ]
    game.reveal_cell(0, 0)
    assert game.flags == [
        [True, False, False],
        [False, False, False],
        [False, False, False]
    ]
def test_reveal_cell_reveals_neighboring_cells_no_bombs():
    game = CampoMinado(root=None, rows=3, cols=3,
                       bombs=0, show_difficulty_menu=None)
    game.field = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    game.reveal_cell(0, 0)
    assert game.flags == [
        [True, False, False],
        [False, False, False],
        [False, False, False]
    ]


def test_reveal_cell_does_not_reveal_bombs():
    game = CampoMinado(root=None, rows=3, cols=3,
                       bombs=0, show_difficulty_menu=None)
    game.field = [
        [-1, -1, -1],
        [-1, 0, -1],
        [-1, -1, -1]
    ]
    game.reveal_cell(1, 1)
    assert game.flags == [
        [False, False, False],
        [False, True, False],
        [False, False, False]
    ]


# Testes para tabuleiro 8x8
def test_reveal_cell_does_not_reveal_bombs_easy_game():
    game = CampoMinado(root=None, rows=8, cols=8,
                       bombs=10, show_difficulty_menu=None)
    game.field = [
        [-1, -1, -1,  0,  0,  0,  0,  0],
        [-1,  0, -1,  0, -1, -1, -1,  0],
        [-1, -1,  0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0, -1,  0],
        [0, -1,  0,  0,  0,  0,  0,  0],
        [0, -1,  0,  0,  0, -1, -1, -1],
        [0,  0,  0, -1,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0]
    ]
    game.reveal_cell(3, 3)
    assert game.flags == [
        [False, False, False,  True,  True,  True,  True,  True],
        [False,  True, False,  True, False, False, False,  True],
        [False, False,  True,  True,  True,  True,  True,  True],
        [True,  True,  True,  True,  True,  True, False,  True],
        [True, False,  True,  True,  True,  True,  True,  True],
        [True, False,  True,  True,  True, False, False, False],
        [True,  True,  True, False,  True,  True,  True,  True],
        [True,  True,  True,  True,  True,  True,  True,  True]
    ]


def test_reveal_cell_corner_cell():
    game = CampoMinado(root=None, rows=8, cols=8,
                       bombs=10, show_difficulty_menu=None)
    game.field = [
        [-1, -1, -1,  0,  0,  0,  0,  0],
        [-1,  0, -1,  0, -1, -1, -1,  0],
        [-1, -1,  0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0, -1,  0],
        [0, -1,  0,  0,  0,  0,  0,  0],
        [0, -1,  0,  0,  0, -1, -1, -1],
        [0,  0,  0, -1,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0]
    ]
    game.reveal_cell(0, 7)
    assert game.flags == [
        [False, False, False,  True,  True,  True,  True,  True],
        [False,  True, False,  True, False, False, False,  True],
        [False, False,  True,  True,  True,  True,  True,  True],
        [True,  True,  True,  True,  True,  True, False,  True],
        [True, False,  True,  True,  True,  True,  True,  True],
        [True, False,  True,  True,  True, False, False, False],
        [True,  True,  True, False,  True,  True,  True,  True],
        [True,  True,  True,  True,  True,  True,  True,  True]
    ]

# tabuleiro sem bombas


def test_reveal_cell_empty_board():
    game = CampoMinado(root=None, rows=8, cols=8,
                       bombs=0, show_difficulty_menu=None)
    game.field = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    game.reveal_cell(3, 3)
    assert game.flags == [
        [True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True]
    ]
# com bombas somente nas bordas


def test_reveal_cell_bombs_on_edges():
    game = CampoMinado(root=None, rows=8, cols=8,
                       bombs=16, show_difficulty_menu=None)
    game.field = [
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0,  0,  0,  0,  0,  0, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1]
    ]
    game.reveal_cell(3, 3)
    assert game.flags == [
        [False, False, False, False, False, False, False, False],
        [False, True, True, True, True, True, True, False],
        [False, True, True, True, True, True, True, False],
        [False, True, True,  True,  True,  True,  True, False],
        [False, True, True,  True,  True,  True,  True, False],
        [False, True, True,  True,  True,  True,  True, False],
        [False, True, True,  True,  True,  True,  True, False],
        [False, False, False, False, False, False, False, False]
    ]


def test_reveal_cell_random_bombs():
    game = CampoMinado(root=None, rows=8, cols=8,
                       bombs=10, show_difficulty_menu=None)
    game.field = [
        [0, -1,  0, -1, -1,  0,  0,  0],
        [-1, 0,  0,  0,  0,  0, -1,  0],
        [0,  0, -1,  0, -1,  0,  0,  0],
        [-1, 0,  0,  0, -1,  0,  0, -1],
        [-1, 0, -1,  0,  0,  0, -1, -1],
        [0,  0, -1, -1, -1,  0, -1,  0],
        [0, -1,  0,  0, -1,  0,  0,  0],
        [0,  0,  0, -1, -1,  0, -1,  0]
    ]
    game.reveal_cell(3, 3)
    assert game.flags == [
        [True, False, True, False, False, True, True, True],
        [False, True, True, True, True, True, False, True],
        [True, True, False, True, False, True, True, True],
        [False, True, True, True, False, True, True, False],
        [False, True, False, True, True, True, False, False],
        [True,  True, False, False, False,  True, False,  True],
        [True, False, True, True, False, True, True, True],
        [True, True, True, False, False, True, False, True]
    ]
def test_reveal_cell_random_bombs_8x8_2():
    game = CampoMinado(root=None, rows=8, cols=8,
                       bombs=10, show_difficulty_menu=None)
    game.field = [
        [0, -1,  0, -1, -1,  0,  0,  0],
        [-1, 0,  0,  0,  0,  0, -1,  0],
        [0,  0, -1,  0, -1,  0,  0,  0],
        [-1, 0,  0,  0, -1,  0,  0, -1],
        [-1, 0, -1,  0,  0,  0, -1, -1],
        [0,  0, -1, -1, -1,  0, -1,  0],
        [0, -1,  0,  0, -1,  0,  0,  0],
        [0,  0,  0, -1, -1,  0, -1,  0]
    ]
    game.reveal_cell(3, 3)
    assert game.flags == [
        [True, False, True, False, False, True, True, True],
        [False, True, True, True, True, True, False, True],
        [True, True, False, True, False, True, True, True],
        [False, True, True, True, False, True, True, False],
        [False, True, False, True, True, True, False, False],
        [True,  True, False, False, False,  True, False,  True],
        [True, False, True, True, False, True, True, True],
        [True, True, True, False, False, True, False, True]
    ]
def test_reveal_cell_random_bombs_8x8_3():
    game = CampoMinado(root=None, rows=8, cols=8,
                       bombs=10, show_difficulty_menu=None)
    game.field = [
        [0, -1,  0, -1, -1,  0,  0,  0],
        [-1, 0,  0,  0,  0,  0, -1,  0],
        [0,  0, -1,  0, -1,  0,  0,  0],
        [-1, 0,  0,  0, -1,  0,  0, -1],
        [-1, 0, -1,  0,  0,  0, -1, -1],
        [0,  0, -1, -1, -1,  0, -1,  0],
        [0, -1,  0,  0, -1,  0,  0,  0],
        [0,  0,  0, -1, -1,  0, -1,  0]
    ]
    game.reveal_cell(3, 3)
    assert game.flags == [
        [True, False, True, False, False, True, True, True],
        [False, True, True, True, True, True, False, True],
        [True, True, False, True, False, True, True, True],
        [False, True, True, True, False, True, True, False],
        [False, True, False, True, True, True, False, False],
        [True,  True, False, False, False,  True, False,  True],
        [True, False, True, True, False, True, True, True],
        [True, True, True, False, False, True, False, True]
    ]

# intermediario com uma bomba


def test_reveal_cell_reveals_zero_neighboring_cells_10x16():
    game = CampoMinado(root=None, rows=10, cols=16,
                       bombs=1, show_difficulty_menu=None)
    game.field = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    game.reveal_cell(5, 8)
    assert game.flags == [
        [True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True]
    ]


def test_medium_game_random_bombs():
    game = CampoMinado(root=None, rows=10, cols=16,
                       bombs=30, show_difficulty_menu=None)

    game.field = [
        [-1, -1, -1, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0, -1, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0, -1, -1, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
    ]
    game.reveal_cell(0, 0)
    assert game.flags == [
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False]
    ]


def test_medium_game_random_bombs_2():
    game = CampoMinado(root=None, rows=10, cols=16,
                       bombs=30, show_difficulty_menu=None)

    game.field = [
        [0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, -1, -1,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0, -1,  0, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1,  0,  0,  0, -1,  0, -1, -1,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1,  0, -1,  0, -1, -1,  0, -1,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  0,  0,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
    ]
    game.reveal_cell(0, 0)
    assert game.flags == [
        [True, True, True, False, False, True, True, True,
            True, True, True, True, True, True, True, True],
        [True, True, True, False, False, True, True, True,
            True, False, True, True, True, True, True, True],
        [True, True, False, True, True, True, True, True,
            False, True, True, True, True, True, True, True],
        [False, True, True, False, True, False, True, False,
            True, True, True, True, True, True, True, True],
        [True, True, False, True, True, True, False, True,
            False, False, True, True, True, True, True, True],
        [True, True, False, True, False, True, False, False,
            True, False, True, True, True, True, True, True],
        [True, True, True, True, True, False, True, False,
            True, True, True, True, True, True, True, True],
        [True, True, True, True, True, False, False, True,
            True, True, True, True, True, True, True, True],
        [False, False, True, True, True, True, True, False,
            False, True, True, True, True, True, True, True],
        [False, True, True, True, True, False, True, True,
            True, True, True, True, True, True, True, True]
    ]


def test_medium_game_random_bombs_3():
    game = CampoMinado(root=None, rows=10, cols=16,
                       bombs=30, show_difficulty_menu=None)

    game.field = [
        [0,  0, -1,  0, -1,  0, -1,  0, -1, -1,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0,  0,  0,  0, -1, -1, -1, -1,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0, -1,  0,  0,  0,  0, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,],
        [0, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0,  0,  0, -1,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0, -1, -1,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
    ]
    game.reveal_cell(0, 0)
    assert game.flags == [
        [True, True, False, True, False, True, False, False,
            False, False, True, True, True, True, True, True],
        [False, True, True, True, True, True, False, False,
            False, False, True, True, True, True, True, True],
        [True, True, False, True, True, True, True, True,
            True, True, True, True, True, True, True, True],
        [True, True, True, False, True, True, True, True,
            True, True, True, True, True, True, True, True],
        [True, False, True, True, True, True, False, False,
            False, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True,
            True, False, True, True, True, True, True, True],
        [True, False, True, False, True, True, True, True,
            True, True, True, True, True, True, True, True],
        [False, True, True, True, True, False, True, True,
            False, False, True, True, True, True, True, True],
        [False, False, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True],
        [False, True, True, False, False, True, False, False,
            True, True, True, True, True, True, True, True]
    ]


def test_medium_game_random_bombs_4():
    game = CampoMinado(root=None, rows=10, cols=16,
                       bombs=30, show_difficulty_menu=None)

    game.field = [
        [-1, -1, -1,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0, -1,  0,  0, -1,  0, -1,  0,  0,  0,  0,  0,  0,],
        [-1,  0, -1,  0,  0, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0, -1,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1, -1, -1,  0,  0, -1, -1, -1,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,],
        [0, -1,  0, -1,  0,  0, -1, -1,  0, -1,  0,  0,  0,  0,  0,  0,],
    ]
    game.reveal_cell(0, 0)
    assert game.flags == [
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False]
    ]


def test_medium_game_random_bombs_5():
    game = CampoMinado(root=None, rows=10, cols=16,
                       bombs=30, show_difficulty_menu=None)

    game.field = [
        [0,  0,  0,  0, -1,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1,  0, -1,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, -1,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  0,  0, -1,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,],
        [0, -1,  0,  0, -1,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0, -1,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1,  0, -1, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,],
    ]
    game.reveal_cell(0, 0)
    assert game.flags == [
        [True, True, True, True, False, True, False, False,
            True, True, True, True, True, True, True, True],
        [True, True, False, True, False, False, True, True,
            True, True, True, True, True, True, True, True],
        [False, False, False, True, False, True, True, True,
            True, False, True, True, True, True, True, True],
        [True, True, True, False, True, True, True, True,
            True, False, True, True, True, True, True, True],
        [False, False, True, True, False, True, True, True,
            True, False, True, True, True, True, True, True],
        [True, False, True, True, False, True, True, False,
            False, True, True, True, True, True, True, True],
        [True, True, True, True, False, True, True, True,
            False, False, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True],
        [True, True, False, False, True, True, True, True,
            True, True, True, True, True, True, True, True],
        [True, True, False, True, False, False, True, True,
            False, True, True, True, True, True, True, True]
    ]

def test_medium_game_random_bombs_6():
    game = CampoMinado(root=None, rows=10, cols=16,
                       bombs=30, show_difficulty_menu=None)

    game.field = [
        [0,  0, -1,  0, -1,  0, -1,  0, -1, -1,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0,  0,  0,  0, -1, -1, -1, -1,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0, -1,  0,  0,  0,  0, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,],
        [0, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0,  0,  0, -1,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0, -1, -1,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
    ]
    game.reveal_cell(0, 0)
    assert game.flags == [
        [True, True, False, True, False, True, False, False,
            False, False, True, True, True, True, True, True],
        [False, True, True, True, True, True, False, False,
            False, False, True, True, True, True, True, True],
        [True, True, False, True, True, True, True, True,
            True, True, True, True, True, True, True, True],
        [True, True, True, False, True, True, True, True,
            True, True, True, True, True, True, True, True],
        [True, False, True, True, True, True, False, False,
            False, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True,
            True, False, True, True, True, True, True, True],
        [True, False, True, False, True, True, True, True,
            True, True, True, True, True, True, True, True],
        [False, True, True, True, True, False, True, True,
            False, False, True, True, True, True, True, True],
        [False, False, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True],
        [False, True, True, False, False, True, False, False,
            True, True, True, True, True, True, True, True]
    ]


def test_medium_game_random_bombs_7():
    game = CampoMinado(root=None, rows=10, cols=16,
                       bombs=30, show_difficulty_menu=None)

    game.field = [
        [-1, -1, -1,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0, -1,  0,  0, -1,  0, -1,  0,  0,  0,  0,  0,  0,],
        [-1,  0, -1,  0,  0, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0, -1,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1, -1, -1,  0,  0, -1, -1, -1,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,],
        [0, -1,  0, -1,  0,  0, -1, -1,  0, -1,  0,  0,  0,  0,  0,  0,],
    ]
    game.reveal_cell(0, 0)
    assert game.flags == [
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False]
    ]
# nivel dificil
def test_reveal_cell_reveals__24x24():
    game = CampoMinado(root=None, rows=24, cols=24,
                       bombs=100, show_difficulty_menu=None)
    game.field = [
        [0, -1,  0,  0, -1,  0,  0,  0, -1,  0,  0,  0,  0,
            0, -1,  0,  0, -1, -1,  0,  0,  0,  0, -1,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0, -1, -
            1, -1, -1,  0, -1,  0, -1,  0,  0,  0,  0,  0,],
        [0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0, -1, -
            1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,],
        [0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0, -1,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1,  0,  0,  0,  0,  0,  0, -1,  0, -1,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, -1,  0,  0,  0,  0, -1,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0, -1,  0,  0,  0, -1,],
        [0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0, -
            1,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0, -1,  0,
            0,  0,  0,  0,  0,  0,  0, -1,  0, -1,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,
            0,  0,  0, -1,  0,  0,  0, -1, -1,  0, -1,],
        [0,  0, -1,  0,  0,  0,  0, -1,  0, -1,  0, -1,  0,
            0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0, -
            1,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0, -1,],
        [0,  0,  0,  0,  0,  0, -1,  0, -1,  0,  0, -1,  0,
            0,  0,  0, -1,  0,  0, -1,  0,  0, -1,  0,],
        [0,  0, -1,  0,  0,  0, -1,  0,  0,  0,  0,  0, -
            1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,
            0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -
            1,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,],
        [0, -1,  0,  0,  0, -1,  0,  0, -1,  0,  0,  0,  0,
            0,  0,  0, -1,  0,  0,  0,  0,  0,  0, -1,],
        [0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1,  0,  0,  0,  0,  0, -1,  0,  0,  0,
            0,  0, -1,  0, -1,  0,  0, -1, -1,  0,  0,  0,],
        [0,  0,  0,  0, -1,  0,  0,  0,  0,  0, -1, -1, -
            1,  0,  0,  0,  0,  0, -1,  0,  0,  0, -1, -1,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0, -1,  0,  0,  0,  0, -1,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0, -
            1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,],
        [0,  0, -1, -1, -1, -1,  0,  0, -1,  0,  0,  0,
            0, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
    ],
    game.reveal_cell(0, 1)  # A célula contém uma bomba, jogo encerrado
    assert game.flags == [
        [False, True,  False,  False, False,  False,  False,  False, False,  False,  False,  False,  False,
            False, False,  False,  False, False, False,  False,  False,  False,  False, False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,
            False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False, False,  False,  False,  False,  False,  False,  False, False, -
        False, False, False,  False, False,  False, False,  False,  False,  False,  False,  False,],
        [False, False, False,  False,  False,  False,  False,  False,  False,  False,  False, False, -
        False,  False,  False,  False,  False,  False,  False,  False,  False,  False, False,  False,],
        [False,  False,  False, False,  False,  False,  False,  False,  False,  False,  False, False,  False,
            False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False, False,  False,  False,  False,  False,  False,  False, False,  False, False,  False,
            False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False, False,  False,  False,  False,  False, False,  False,  False,  False,  False,
            False,  False,  False,  False,  False,  False, False,  False,  False,  False, False,],
        [False,  False,  False, False,  False,  False,  False,  False,  False,  False,  False,  False, -
        False,  False,  False,  False, False, False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False,  False, False,  False,  False,  False,  False,  False, False,  False,
            False,  False,  False,  False,  False,  False,  False, False,  False, False,  False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False, False,  False,  False,
            False,  False,  False, False,  False,  False,  False, False, False,  False, False,],
        [False,  False, False,  False,  False,  False,  False, False,  False, False,  False, False,  False,
            False,  False,  False,  False,  False,  False,  False,  False, False,  False,  False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False, False,  False, -
        False,  False,  False,  False,  False,  False,  False, False,  False,  False,  False, False,],
        [False,  False,  False,  False,  False,  False, False,  False, False,  False,  False, False,  False,
            False,  False,  False, False,  False,  False, False,  False,  False, False,  False,],
        [False,  False, False,  False,  False,  False, False,  False,  False,  False,  False,  False, -
        False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False,  False, False,  False,  False,  False,  False,  False,  False,  False,
            False, False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False, -
        False,  False,  False,  False,  False,  False, False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False, False, False,  False,  False,  False,  False,  False,  False,  False,
            False,  False,  False,  False,  False,  False, False,  False,  False,  False,  False,],
        [False, False,  False,  False,  False, False,  False,  False, False,  False,  False,  False,  False,
            False,  False,  False, False,  False,  False,  False,  False,  False,  False, False,],
        [False,  False,  False, False,  False,  False,  False,  False,  False,  False,  False,  False,  False,
            False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False, False, False,  False,  False,  False,  False,  False, False,  False,  False,  False,
            False,  False, False,  False, False,  False,  False, False, False,  False,  False,  False,],
        [False,  False,  False,  False, False,  False,  False,  False,  False,  False, False, False, -
        False,  False,  False,  False,  False,  False, False,  False,  False,  False, False, False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,
            False,  False,  False, False,  False,  False,  False,  False, False,  False,  False,],
        [False,  False,  False,  False,  False,  False,  False,  False, False,  False,  False,  False, -
        False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False, False,],
        [False,  False, False, False, False, False,  False,  False, False,  False,  False,  False,
            False, False, False, False,  False,  False,  False,  False,  False,  False,  False,  False,],
    ]
def test_reveal_cell_reveals__24x24_2():
    game = CampoMinado(root=None, rows=24, cols=24,
                       bombs=100, show_difficulty_menu=None)
    game.field = [
        [0, -1,  0,  0, -1,  0,  0,  0, -1,  0,  0,  0,  0,
            0, -1,  0,  0, -1, -1,  0,  0,  0,  0, -1,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0, -1, -
            1, -1, -1,  0, -1,  0, -1,  0,  0,  0,  0,  0,],
        [0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0, -1, -
            1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,],
        [0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0, -1,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1,  0,  0,  0,  0,  0,  0, -1,  0, -1,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, -1,  0,  0,  0,  0, -1,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0, -1,  0,  0,  0, -1,],
        [0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0, -
            1,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0, -1,  0,
            0,  0,  0,  0,  0,  0,  0, -1,  0, -1,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,
            0,  0,  0, -1,  0,  0,  0, -1, -1,  0, -1,],
        [0,  0, -1,  0,  0,  0,  0, -1,  0, -1,  0, -1,  0,
            0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0, -
            1,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0, -1,],
        [0,  0,  0,  0,  0,  0, -1,  0, -1,  0,  0, -1,  0,
            0,  0,  0, -1,  0,  0, -1,  0,  0, -1,  0,],
        [0,  0, -1,  0,  0,  0, -1,  0,  0,  0,  0,  0, -
            1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,
            0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -
            1,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,],
        [0, -1,  0,  0,  0, -1,  0,  0, -1,  0,  0,  0,  0,
            0,  0,  0, -1,  0,  0,  0,  0,  0,  0, -1,],
        [0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1,  0,  0,  0,  0,  0, -1,  0,  0,  0,
            0,  0, -1,  0, -1,  0,  0, -1, -1,  0,  0,  0,],
        [0,  0,  0,  0, -1,  0,  0,  0,  0,  0, -1, -1, -
            1,  0,  0,  0,  0,  0, -1,  0,  0,  0, -1, -1,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0, -1,  0,  0,  0,  0, -1,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0, -
            1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,],
        [0,  0, -1, -1, -1, -1,  0,  0, -1,  0,  0,  0,
            0, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
    ],
    game.reveal_cell(0, 1)  # A célula contém uma bomba, jogo encerrado
    assert game.flags == [
        [False, True,  False,  False, False,  False,  False,  False, False,  False,  False,  False,  False,
            False, False,  False,  False, False, False,  False,  False,  False,  False, False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,
            False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False, False,  False,  False,  False,  False,  False,  False, False, -
        False, False, False,  False, False,  False, False,  False,  False,  False,  False,  False,],
        [False, False, False,  False,  False,  False,  False,  False,  False,  False,  False, False, -
        False,  False,  False,  False,  False,  False,  False,  False,  False,  False, False,  False,],
        [False,  False,  False, False,  False,  False,  False,  False,  False,  False,  False, False,  False,
            False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False, False,  False,  False,  False,  False,  False,  False, False,  False, False,  False,
            False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False, False,  False,  False,  False,  False, False,  False,  False,  False,  False,
            False,  False,  False,  False,  False,  False, False,  False,  False,  False, False,],
        [False,  False,  False, False,  False,  False,  False,  False,  False,  False,  False,  False, -
        False,  False,  False,  False, False, False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False,  False, False,  False,  False,  False,  False,  False, False,  False,
            False,  False,  False,  False,  False,  False,  False, False,  False, False,  False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False, False,  False,  False,
            False,  False,  False, False,  False,  False,  False, False, False,  False, False,],
        [False,  False, False,  False,  False,  False,  False, False,  False, False,  False, False,  False,
            False,  False,  False,  False,  False,  False,  False,  False, False,  False,  False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False, False,  False, -
        False,  False,  False,  False,  False,  False,  False, False,  False,  False,  False, False,],
        [False,  False,  False,  False,  False,  False, False,  False, False,  False,  False, False,  False,
            False,  False,  False, False,  False,  False, False,  False,  False, False,  False,],
        [False,  False, False,  False,  False,  False, False,  False,  False,  False,  False,  False, -
        False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False,  False, False,  False,  False,  False,  False,  False,  False,  False,
            False, False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False, -
        False,  False,  False,  False,  False,  False, False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False, False, False,  False,  False,  False,  False,  False,  False,  False,
            False,  False,  False,  False,  False,  False, False,  False,  False,  False,  False,],
        [False, False,  False,  False,  False, False,  False,  False, False,  False,  False,  False,  False,
            False,  False,  False, False,  False,  False,  False,  False,  False,  False, False,],
        [False,  False,  False, False,  False,  False,  False,  False,  False,  False,  False,  False,  False,
            False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False, False, False,  False,  False,  False,  False,  False, False,  False,  False,  False,
            False,  False, False,  False, False,  False,  False, False, False,  False,  False,  False,],
        [False,  False,  False,  False, False,  False,  False,  False,  False,  False, False, False, -
        False,  False,  False,  False,  False,  False, False,  False,  False,  False, False, False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,
            False,  False,  False, False,  False,  False,  False,  False, False,  False,  False,],
        [False,  False,  False,  False,  False,  False,  False,  False, False,  False,  False,  False, -
        False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False, False,],
        [False,  False, False, False, False, False,  False,  False, False,  False,  False,  False,
            False, False, False, False,  False,  False,  False,  False,  False,  False,  False,  False,],
    ]
def test_reveal_cell_reveals__24x24_3():
    game = CampoMinado(root=None, rows=24, cols=24,
                       bombs=100, show_difficulty_menu=None)
    game.field = [
        [0, -1,  0,  0, -1,  0,  0,  0, -1,  0,  0,  0,  0,
            0, -1,  0,  0, -1, -1,  0,  0,  0,  0, -1,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0, -1, -
            1, -1, -1,  0, -1,  0, -1,  0,  0,  0,  0,  0,],
        [0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0, -1, -
            1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,],
        [0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0, -1,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1,  0,  0,  0,  0,  0,  0, -1,  0, -1,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, -1,  0,  0,  0,  0, -1,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0, -1,  0,  0,  0, -1,],
        [0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0, -
            1,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0, -1,  0,
            0,  0,  0,  0,  0,  0,  0, -1,  0, -1,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,
            0,  0,  0, -1,  0,  0,  0, -1, -1,  0, -1,],
        [0,  0, -1,  0,  0,  0,  0, -1,  0, -1,  0, -1,  0,
            0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0, -
            1,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0, -1,],
        [0,  0,  0,  0,  0,  0, -1,  0, -1,  0,  0, -1,  0,
            0,  0,  0, -1,  0,  0, -1,  0,  0, -1,  0,],
        [0,  0, -1,  0,  0,  0, -1,  0,  0,  0,  0,  0, -
            1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,
            0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -
            1,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,],
        [0, -1,  0,  0,  0, -1,  0,  0, -1,  0,  0,  0,  0,
            0,  0,  0, -1,  0,  0,  0,  0,  0,  0, -1,],
        [0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1,  0,  0,  0,  0,  0, -1,  0,  0,  0,
            0,  0, -1,  0, -1,  0,  0, -1, -1,  0,  0,  0,],
        [0,  0,  0,  0, -1,  0,  0,  0,  0,  0, -1, -1, -
            1,  0,  0,  0,  0,  0, -1,  0,  0,  0, -1, -1,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0, -1,  0,  0,  0,  0, -1,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0, -
            1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,],
        [0,  0, -1, -1, -1, -1,  0,  0, -1,  0,  0,  0,
            0, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
    ],
    game.reveal_cell(0, 1)  # A célula contém uma bomba, jogo encerrado
    assert game.flags == [
        [False, True,  False,  False, False,  False,  False,  False, False,  False,  False,  False,  False,
            False, False,  False,  False, False, False,  False,  False,  False,  False, False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,
            False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False, False,  False,  False,  False,  False,  False,  False, False, -
        False, False, False,  False, False,  False, False,  False,  False,  False,  False,  False,],
        [False, False, False,  False,  False,  False,  False,  False,  False,  False,  False, False, -
        False,  False,  False,  False,  False,  False,  False,  False,  False,  False, False,  False,],
        [False,  False,  False, False,  False,  False,  False,  False,  False,  False,  False, False,  False,
            False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False, False,  False,  False,  False,  False,  False,  False, False,  False, False,  False,
            False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False, False,  False,  False,  False,  False, False,  False,  False,  False,  False,
            False,  False,  False,  False,  False,  False, False,  False,  False,  False, False,],
        [False,  False,  False, False,  False,  False,  False,  False,  False,  False,  False,  False, -
        False,  False,  False,  False, False, False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False,  False, False,  False,  False,  False,  False,  False, False,  False,
            False,  False,  False,  False,  False,  False,  False, False,  False, False,  False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False, False,  False,  False,
            False,  False,  False, False,  False,  False,  False, False, False,  False, False,],
        [False,  False, False,  False,  False,  False,  False, False,  False, False,  False, False,  False,
            False,  False,  False,  False,  False,  False,  False,  False, False,  False,  False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False, False,  False, -
        False,  False,  False,  False,  False,  False,  False, False,  False,  False,  False, False,],
        [False,  False,  False,  False,  False,  False, False,  False, False,  False,  False, False,  False,
            False,  False,  False, False,  False,  False, False,  False,  False, False,  False,],
        [False,  False, False,  False,  False,  False, False,  False,  False,  False,  False,  False, -
        False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False,  False, False,  False,  False,  False,  False,  False,  False,  False,
            False, False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False, -
        False,  False,  False,  False,  False,  False, False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False, False, False,  False,  False,  False,  False,  False,  False,  False,
            False,  False,  False,  False,  False,  False, False,  False,  False,  False,  False,],
        [False, False,  False,  False,  False, False,  False,  False, False,  False,  False,  False,  False,
            False,  False,  False, False,  False,  False,  False,  False,  False,  False, False,],
        [False,  False,  False, False,  False,  False,  False,  False,  False,  False,  False,  False,  False,
            False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False, False, False,  False,  False,  False,  False,  False, False,  False,  False,  False,
            False,  False, False,  False, False,  False,  False, False, False,  False,  False,  False,],
        [False,  False,  False,  False, False,  False,  False,  False,  False,  False, False, False, -
        False,  False,  False,  False,  False,  False, False,  False,  False,  False, False, False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,
            False,  False,  False, False,  False,  False,  False,  False, False,  False,  False,],
        [False,  False,  False,  False,  False,  False,  False,  False, False,  False,  False,  False, -
        False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False, False,],
        [False,  False, False, False, False, False,  False,  False, False,  False,  False,  False,
            False, False, False, False,  False,  False,  False,  False,  False,  False,  False,  False,],
    ]
def test_reveal_cell_reveals__24x24_4():
    game = CampoMinado(root=None, rows=24, cols=24,
                       bombs=100, show_difficulty_menu=None)
    game.field = [
        [0, -1,  0,  0, -1,  0,  0,  0, -1,  0,  0,  0,  0,
            0, -1,  0,  0, -1, -1,  0,  0,  0,  0, -1,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0, -1, -
            1, -1, -1,  0, -1,  0, -1,  0,  0,  0,  0,  0,],
        [0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0, -1, -
            1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,],
        [0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0, -1,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1,  0,  0,  0,  0,  0,  0, -1,  0, -1,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, -1,  0,  0,  0,  0, -1,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0, -1,  0,  0,  0, -1,],
        [0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0, -
            1,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0, -1,  0,
            0,  0,  0,  0,  0,  0,  0, -1,  0, -1,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,
            0,  0,  0, -1,  0,  0,  0, -1, -1,  0, -1,],
        [0,  0, -1,  0,  0,  0,  0, -1,  0, -1,  0, -1,  0,
            0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0, -
            1,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0, -1,],
        [0,  0,  0,  0,  0,  0, -1,  0, -1,  0,  0, -1,  0,
            0,  0,  0, -1,  0,  0, -1,  0,  0, -1,  0,],
        [0,  0, -1,  0,  0,  0, -1,  0,  0,  0,  0,  0, -
            1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,
            0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -
            1,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,],
        [0, -1,  0,  0,  0, -1,  0,  0, -1,  0,  0,  0,  0,
            0,  0,  0, -1,  0,  0,  0,  0,  0,  0, -1,],
        [0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1,  0,  0,  0,  0,  0, -1,  0,  0,  0,
            0,  0, -1,  0, -1,  0,  0, -1, -1,  0,  0,  0,],
        [0,  0,  0,  0, -1,  0,  0,  0,  0,  0, -1, -1, -
            1,  0,  0,  0,  0,  0, -1,  0,  0,  0, -1, -1,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0, -1,  0,  0,  0,  0, -1,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0, -
            1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,],
        [0,  0, -1, -1, -1, -1,  0,  0, -1,  0,  0,  0,
            0, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
    ],
    game.reveal_cell(0, 1)  # A célula contém uma bomba, jogo encerrado
    assert game.flags == [
        [False, True,  False,  False, False,  False,  False,  False, False,  False,  False,  False,  False,
            False, False,  False,  False, False, False,  False,  False,  False,  False, False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,
            False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False, False,  False,  False,  False,  False,  False,  False, False, -
        False, False, False,  False, False,  False, False,  False,  False,  False,  False,  False,],
        [False, False, False,  False,  False,  False,  False,  False,  False,  False,  False, False, -
        False,  False,  False,  False,  False,  False,  False,  False,  False,  False, False,  False,],
        [False,  False,  False, False,  False,  False,  False,  False,  False,  False,  False, False,  False,
            False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False, False,  False,  False,  False,  False,  False,  False, False,  False, False,  False,
            False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False, False,  False,  False,  False,  False, False,  False,  False,  False,  False,
            False,  False,  False,  False,  False,  False, False,  False,  False,  False, False,],
        [False,  False,  False, False,  False,  False,  False,  False,  False,  False,  False,  False, -
        False,  False,  False,  False, False, False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False,  False, False,  False,  False,  False,  False,  False, False,  False,
            False,  False,  False,  False,  False,  False,  False, False,  False, False,  False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False, False,  False,  False,
            False,  False,  False, False,  False,  False,  False, False, False,  False, False,],
        [False,  False, False,  False,  False,  False,  False, False,  False, False,  False, False,  False,
            False,  False,  False,  False,  False,  False,  False,  False, False,  False,  False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False, False,  False, -
        False,  False,  False,  False,  False,  False,  False, False,  False,  False,  False, False,],
        [False,  False,  False,  False,  False,  False, False,  False, False,  False,  False, False,  False,
            False,  False,  False, False,  False,  False, False,  False,  False, False,  False,],
        [False,  False, False,  False,  False,  False, False,  False,  False,  False,  False,  False, -
        False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False,  False, False,  False,  False,  False,  False,  False,  False,  False,
            False, False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False, -
        False,  False,  False,  False,  False,  False, False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False, False, False,  False,  False,  False,  False,  False,  False,  False,
            False,  False,  False,  False,  False,  False, False,  False,  False,  False,  False,],
        [False, False,  False,  False,  False, False,  False,  False, False,  False,  False,  False,  False,
            False,  False,  False, False,  False,  False,  False,  False,  False,  False, False,],
        [False,  False,  False, False,  False,  False,  False,  False,  False,  False,  False,  False,  False,
            False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False, False, False,  False,  False,  False,  False,  False, False,  False,  False,  False,
            False,  False, False,  False, False,  False,  False, False, False,  False,  False,  False,],
        [False,  False,  False,  False, False,  False,  False,  False,  False,  False, False, False, -
        False,  False,  False,  False,  False,  False, False,  False,  False,  False, False, False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,
            False,  False,  False, False,  False,  False,  False,  False, False,  False,  False,],
        [False,  False,  False,  False,  False,  False,  False,  False, False,  False,  False,  False, -
        False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False, False,],
        [False,  False, False, False, False, False,  False,  False, False,  False,  False,  False,
            False, False, False, False,  False,  False,  False,  False,  False,  False,  False,  False,],
    ]
def test_reveal_cell_reveals__24x24_5():
    game = CampoMinado(root=None, rows=24, cols=24,
                       bombs=100, show_difficulty_menu=None)
    game.field = [
        [0, -1,  0,  0, -1,  0,  0,  0, -1,  0,  0,  0,  0,
            0, -1,  0,  0, -1, -1,  0,  0,  0,  0, -1,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0, -1, -
            1, -1, -1,  0, -1,  0, -1,  0,  0,  0,  0,  0,],
        [0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0, -1, -
            1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,],
        [0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0, -1,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1,  0,  0,  0,  0,  0,  0, -1,  0, -1,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, -1,  0,  0,  0,  0, -1,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0, -1,  0,  0,  0, -1,],
        [0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0, -
            1,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0, -1,  0,
            0,  0,  0,  0,  0,  0,  0, -1,  0, -1,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,
            0,  0,  0, -1,  0,  0,  0, -1, -1,  0, -1,],
        [0,  0, -1,  0,  0,  0,  0, -1,  0, -1,  0, -1,  0,
            0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0, -
            1,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0, -1,],
        [0,  0,  0,  0,  0,  0, -1,  0, -1,  0,  0, -1,  0,
            0,  0,  0, -1,  0,  0, -1,  0,  0, -1,  0,],
        [0,  0, -1,  0,  0,  0, -1,  0,  0,  0,  0,  0, -
            1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,
            0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -
            1,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,],
        [0, -1,  0,  0,  0, -1,  0,  0, -1,  0,  0,  0,  0,
            0,  0,  0, -1,  0,  0,  0,  0,  0,  0, -1,],
        [0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1,  0,  0,  0,  0,  0, -1,  0,  0,  0,
            0,  0, -1,  0, -1,  0,  0, -1, -1,  0,  0,  0,],
        [0,  0,  0,  0, -1,  0,  0,  0,  0,  0, -1, -1, -
            1,  0,  0,  0,  0,  0, -1,  0,  0,  0, -1, -1,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0, -1,  0,  0,  0,  0, -1,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0, -
            1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,],
        [0,  0, -1, -1, -1, -1,  0,  0, -1,  0,  0,  0,
            0, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
    ],
    game.reveal_cell(0, 1)  # A célula contém uma bomba, jogo encerrado
    assert game.flags == [
        [False, True,  False,  False, False,  False,  False,  False, False,  False,  False,  False,  False,
            False, False,  False,  False, False, False,  False,  False,  False,  False, False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,
            False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False, False,  False,  False,  False,  False,  False,  False, False, -
        False, False, False,  False, False,  False, False,  False,  False,  False,  False,  False,],
        [False, False, False,  False,  False,  False,  False,  False,  False,  False,  False, False, -
        False,  False,  False,  False,  False,  False,  False,  False,  False,  False, False,  False,],
        [False,  False,  False, False,  False,  False,  False,  False,  False,  False,  False, False,  False,
            False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False, False,  False,  False,  False,  False,  False,  False, False,  False, False,  False,
            False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False, False,  False,  False,  False,  False, False,  False,  False,  False,  False,
            False,  False,  False,  False,  False,  False, False,  False,  False,  False, False,],
        [False,  False,  False, False,  False,  False,  False,  False,  False,  False,  False,  False, -
        False,  False,  False,  False, False, False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False,  False, False,  False,  False,  False,  False,  False, False,  False,
            False,  False,  False,  False,  False,  False,  False, False,  False, False,  False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False, False,  False,  False,
            False,  False,  False, False,  False,  False,  False, False, False,  False, False,],
        [False,  False, False,  False,  False,  False,  False, False,  False, False,  False, False,  False,
            False,  False,  False,  False,  False,  False,  False,  False, False,  False,  False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False, False,  False, -
        False,  False,  False,  False,  False,  False,  False, False,  False,  False,  False, False,],
        [False,  False,  False,  False,  False,  False, False,  False, False,  False,  False, False,  False,
            False,  False,  False, False,  False,  False, False,  False,  False, False,  False,],
        [False,  False, False,  False,  False,  False, False,  False,  False,  False,  False,  False, -
        False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False,  False, False,  False,  False,  False,  False,  False,  False,  False,
            False, False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False, -
        False,  False,  False,  False,  False,  False, False,  False,  False,  False,  False,  False,],
        [False,  False,  False,  False, False, False,  False,  False,  False,  False,  False,  False,  False,
            False,  False,  False,  False,  False,  False, False,  False,  False,  False,  False,],
        [False, False,  False,  False,  False, False,  False,  False, False,  False,  False,  False,  False,
            False,  False,  False, False,  False,  False,  False,  False,  False,  False, False,],
        [False,  False,  False, False,  False,  False,  False,  False,  False,  False,  False,  False,  False,
            False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,],
        [False, False, False,  False,  False,  False,  False,  False, False,  False,  False,  False,
            False,  False, False,  False, False,  False,  False, False, False,  False,  False,  False,],
        [False,  False,  False,  False, False,  False,  False,  False,  False,  False, False, False, -
        False,  False,  False,  False,  False,  False, False,  False,  False,  False, False, False,],
        [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,
            False,  False,  False, False,  False,  False,  False,  False, False,  False,  False,],
        [False,  False,  False,  False,  False,  False,  False,  False, False,  False,  False,  False, -
        False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False, False,],
        [False,  False, False, False, False, False,  False,  False, False,  False,  False,  False,
            False, False, False, False,  False,  False,  False,  False,  False,  False,  False,  False,],
    ]
