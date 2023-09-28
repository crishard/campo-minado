import pytest
from functions.calculate_numbers import calculate_numbers_function


@pytest.mark.parametrize("input_field, rows, cols, expected_field", [


    # teste matriz 6x6 - 8 bombas
    ([
        [-1, 0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,],
        [0,  0,  0, -1, -1,  0,],
        [0, -1,  0,  0,  0,  0,],
        [0,  0,  0, -1,  0,  0,],
        [-1, 0,  0, -1,  0, -1],
    ], 6, 6, [
        [-1, 1,  0,  0,  0,  0,],
        [1,  1,  1,  2,  2,  1,],
        [1,  1,  2, -1, -1,  1,],
        [1, -1,  3,  3,  3,  1,],
        [2,  2,  3, -1,  3,  1,],
        [-1, 1,  2, -1,  3, -1],
    ]),

    # teste matriz 17x17
    # teste matriz 18x18
    # teste matriz 22x22
    # teste matriz 23x23


    # para o tabuleiro de nível intermediário - 10 testes no total



    # teste matriz 25x25
    # teste matriz 26x26

])
def test_calculate_numbers(input_field, rows, cols, expected_field):
    calculate_numbers_function(input_field, rows, cols)
    assert input_field == expected_field
