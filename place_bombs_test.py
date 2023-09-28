from functions.place_bombs import place_bombs_function


def test_place_bombs_valid_counts():
    field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    bombs = 5
    place_bombs_function(field, bombs)
    bomb_count = sum(row.count(-1) for row in field)
    assert bomb_count == bombs