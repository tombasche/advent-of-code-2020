from functools import reduce
from typing import List

from shared.file_reading import read_file


def count_trees(lines: List[str], right: int = 3, down: int = 1) -> int:
    trees = 0
    starting_pos = 0  # first square + 3

    extensions = 2
    i = 0
    while i < len(lines) - 1:

        line = lines[i]
        starting_pos += right
        i += down

        if i > len(lines):
            return trees

        line = lines[i]
        if starting_pos >= len(line):
            line = infer_rest_of_path(line, extensions * 4)
            extensions += 1

        trees += tree(line, starting_pos)

    return trees


def tree(line: str, position: int) -> int:
    return 1 if line[position] == "#" else 0


def infer_rest_of_path(line: str, amount: int) -> str:
    return line * amount


def main():
    lines = read_file()
    slopes = [
        (1, 1),  # 2
        (3, 1),  # 7
        (5, 1),  # 3
        (7, 1),  # 4
        (1, 2),  # 2
    ]
    trees = []
    for right, down in slopes:
        trees.append(count_trees(lines, right, down))

    print(trees)
    print(reduce(lambda x, y: x * y, trees))


if __name__ == '__main__':
    main()
