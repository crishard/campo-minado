import pytest
from campo_minado import CampoMinado


def test_reveal_cell_reveals_zero_bombs_1x1():
    game = CampoMinado(root=None, rows=1, cols=1,
                       bombs=0, show_difficulty_menu=None)
    game.field = [
        [0],
    ]
    game.reveal_cell(0, 0)  # a célula contem bomba, jogo encerrado
    assert game.flags == [
        [True],

    ]

def test_reveal_cell_reveals_zero_bombs_3x3():
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


def test_reveal_cell_reveals_zero_2x2():
    game = CampoMinado(root=None, rows=2, cols=2,
                       bombs=1, show_difficulty_menu=None)
    game.field = [
        [0, 0,],
        [0, -1],
    ]
    game.reveal_cell(1, 1)  # a célula contem bomba, jogo encerrado
    assert game.flags == [
        [False, False],
        [False, False],
    ]


def test_reveal_cell_reveals_zero_4x4():
    game = CampoMinado(root=None, rows=4, cols=4,
                       bombs=1, show_difficulty_menu=None)
    game.field = [
        [0, 0, 0, 0],
        [0, -1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    game.reveal_cell(1, 1)  # a célula contem bomba, jogo encerrado
    assert game.flags == [
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False]
    ]


def test_reveal_cell_reveals_zero_5x5():
    game = CampoMinado(root=None, rows=5, cols=5,
                       bombs=1, show_difficulty_menu=None)
    game.field = [
        [0, 0, 0, 0, 0,],
        [0, -1, 0, 0,0,],
        [0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0,]
    ]
    game.reveal_cell(1, 1)  # a célula contem bomba, jogo encerrado
    assert game.flags == [
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
    ]

def test_reveal_cell_reveals_7x7():
    game = CampoMinado(root=None, rows=7, cols=7,
                       bombs=1, show_difficulty_menu=None)
    game.field = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, -1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 0]
    ]
    game.reveal_cell(1, 1)  # a célula contem bomba, jogo encerrado
    assert game.flags == [
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False],
    ]


def test_reveal_cell_reveals_9x9():
    game = CampoMinado(root=None, rows=9, cols=9,
                       bombs=1, show_difficulty_menu=None)
    game.field = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, -1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    game.reveal_cell(1, 1)  # a célula contem bomba, jogo encerrado
    assert game.flags == [
        [False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False],
    ]



def test_reveal_cell_reveals_10x17():
    game = CampoMinado(root=None, rows=10, cols=17,
                       bombs=1, show_difficulty_menu=None)
    game.field = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    game.reveal_cell(1, 1)  # a célula contem bomba, jogo encerrado
    assert game.flags == [
        [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    ]
