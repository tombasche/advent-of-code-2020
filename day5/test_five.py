import pytest

from day5.five import parse, bsp, seat_id, find_seat

bp1 = 'BFFFBBFRRR'  # row 70, column 7, seat ID 567
bp2 = 'FFFBBBFRRR'  # row 14, column 7, seat ID 119
bp3 = 'BBFFBBFRLL'  # row 102, column 4, seat ID 820


@pytest.mark.parametrize('boarding_pass, expected_row, expected_column, expected_seat_id', [
    (bp1, 70, 7, 567),
    (bp2, 14, 7, 119),
    (bp3, 102, 4, 820),
])
def test_decode_seat_number(boarding_pass, expected_row, expected_column, expected_seat_id):
    row, column = parse(boarding_pass)
    assert row == expected_row
    assert column == expected_column
    assert seat_id(row, column) == expected_seat_id


@pytest.mark.parametrize('r, expected', [
    ('FFFBBBF', 14),
    ('FBFBBFF', 44),
    ('FBFBBFB', 45),
    ('BBFFBBF', 102),
])
def test_columns(r, expected):
    assert bsp(r, 'F', 'B') == expected


@pytest.mark.parametrize('r, expected', [
    ('RRR', 7),
    ('RLL', 4),
    ('RLR', 5),
])
def test_rows(r, expected):
    assert bsp(r, 'L', 'R', range=7) == expected


def test_find_seat():
    seats = [33, 34, 35, 36, 38, 39, 40, 41, 42, 43]
    assert find_seat(seats) == 37
