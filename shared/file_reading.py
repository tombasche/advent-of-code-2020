from typing import List


def strip_newlines(strings: List[str]) -> List[str]:
    return list(map(lambda s: s.strip(), strings))


def read_file(filename: str = 'puzzle.txt') -> List[str]:
    strings = []
    with open(filename) as f:
        for line in f.readlines():
            strings.append(line)
    return strip_newlines(strings)


def read_file_delimited_by_space(filename: str = 'puzzle.txt') -> List[str]:
    strings = []
    with open(filename) as f:
        chunk = ""
        for line in f.readlines():

            if line == '\n':
                strings.append(chunk)
                chunk = ""
            else:
                chunk += line

    return strip_newlines(strings)
