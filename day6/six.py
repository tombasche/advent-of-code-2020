from functools import reduce
from typing import List

from shared.file_reading import read_file_delimited_by_space, read_file


def group_answers(group: str) -> int:

    seen = {}
    for letter in group:
        if letter == "\n":
            continue
        seen[letter] = 1
    return sum(seen.values())


def count_responses(groups: List[str]) -> int:
    total = 0
    for group in groups:
        total += group_answers(group)
    return total


def everyone_answered(groups: List[str]) -> int:
    # count the letters that are in every group

    total = 0
    groups = [set(g) for g in groups]
    candidate = groups[0]
    for group in groups[1:]:

        candidate &= group
        total += len(candidate)
    return total



def main():
    with open('puzzle.txt') as f:
        responses = f.read().split('\n\n')

    responses = list(map(lambda l: l.replace('\n', ''), responses))
    total = count_responses(responses)
    print(total)


if __name__ == "__main__":
    main()

