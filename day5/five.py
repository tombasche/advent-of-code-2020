from math import floor
from typing import Tuple, List

from shared.file_reading import read_file


def parse(bsp_str: str) -> Tuple[int, int]:
    row, column = bsp_str[:-3], bsp_str[-3:]
    row = bsp(row, 'F', 'B')
    column = bsp(column, 'L', 'R', range=7)
    return row, column


def seat_id(row: int, column: int) -> int:
    return (row * 8) + column


def bsp(s: str, u: str, l: str, range: int = 127) -> int:
    upper = range
    lower = 0
    for letter in s:

        if letter == u:
            upper -= floor((upper - lower) / 2) + 1

        if letter == l:
            lower += floor((upper - lower) / 2) + 1

    if upper == lower:
        return upper


def find_seat(seats: List[int]) -> int:
    seats = sorted(seats)
    for i in range(seats[0], seats[-1]):
        if i not in seats:
            return i


def main():
    boarding_passes = read_file()
    seat_ids = [seat_id(*parse(bp)) for bp in boarding_passes]
    # Part 1
    print(max(seat_ids))
    my_seat = find_seat(seat_ids)
    print(my_seat)


main()
