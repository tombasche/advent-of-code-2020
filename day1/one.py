from typing import List

def fix_expense_report(inputs: List[int]) -> int:
    result = 0
    for i in inputs:
        for j in inputs:
            for k in inputs:
                if i + j + k == 2020:
                    result =  i * j * k
    return result


def read_file(filename: str = 'puzzle.txt') -> List[str]:
    strings = []
    with open(filename) as f:
        for line in f.readlines():
            strings.append(line)
    return strip_newlines(strings)

def strip_newlines(strings: List[str]) -> List[str]:
    return map(lambda s: s.strip(), strings)

def convert_to_int(strings: List[str]) -> List[int]:
    return list(map(int, strings))

def main():
    result = fix_expense_report(convert_to_int(read_file()))
    print(result)

if __name__ == "__main__":
    main()