from functions.place_bombs import place_bombs_function


def test_place_bombs_valid_counts():
    field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    bombs = 5
    place_bombs_function(field, bombs)
    bomb_count = sum(row.count(-1) for row in field)
    assert bomb_count == bombs

def test_place_bombs_valid_positions():
    field = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    bombs = 5
    place_bombs_function(field, bombs)
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == -1:
                assert 0 <= row < len(field) and 0 <= col < len(field[row])
                
def test_place_bombs_empty_field():
    field = []
    bombs = 0
    place_bombs_function(field, bombs)
    assert field == []


def test_place_bombs_all_bombs():
    field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    bombs = 9
    place_bombs_function(field, bombs)
    bomb_count = sum(row.count(-1) for row in field)
    assert bomb_count == 9


def test_place_bombs_no_bombs():
    field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    bombs = 0
    place_bombs_function(field, bombs)
    bomb_count = sum(row.count(-1) for row in field)
    assert bomb_count == 0


def test_place_bombs_bomb_count():
    field = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    bombs = 5
    place_bombs_function(field, bombs)
    bomb_count = sum(row.count(-1) for row in field)
    assert bomb_count == bombs


def test_place_bombs_no_extra_bombs():
    field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    bombs = 2
    place_bombs_function(field, bombs)
    bomb_count = sum(row.count(-1) for row in field)
    assert bomb_count == bombs

def test_place_bombs_negative_bombs():

    field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    bombs = -1
    place_bombs_function(field, bombs)
    bomb_count = sum(row.count(-1) for row in field)
    assert bomb_count == 0


def test_place_bombs_valid_range():
    field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    bombs = 5
    place_bombs_function(field, bombs)
    for row in field:
        for cell in row:
            if cell == -1:
                assert -1 <= cell <= 8
