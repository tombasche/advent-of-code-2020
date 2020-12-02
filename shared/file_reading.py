from typing import List

def strip_newlines(strings: List[str]) -> List[str]:
    return map(lambda s: s.strip(), strings)


def read_file(filename: str = 'puzzle.txt') -> List[str]:
    strings = []
    with open(filename) as f:
        for line in f.readlines():
            strings.append(line)
    return strip_newlines(strings)
