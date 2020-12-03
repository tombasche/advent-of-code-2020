from typing import Type
from functools import partial
from shared.file_reading import read_file


class BasePolicy:
    def __init__(self, first: int, second: int, letter: str, password: str):
        self._first = first 
        self._second = second
        self._letter = letter
        self._password = password

    def __eq__(self, other: 'BasePolicy') -> bool:
        if other is None:
            return False
        return (
            self._first == other._first and 
            self._second == other._second and 
            self._letter == other._letter and 
            self._password == other._password
        )

class Policy(BasePolicy):

    def check_valid(self) -> bool:
        occurrences = 0
        for c in self._password:
            if c == self._letter:
                occurrences += 1
        return self._first <= occurrences <= self._second

class PositionPolicy(BasePolicy):
    
    def check_valid(self) -> bool:
        first_letter = self._password[self._first - 1]
        second_letter = self._password[self._second - 1]

        first_matches = first_letter == self._letter
        second_matches = second_letter == self._letter
        return any([first_matches, second_matches]) and not all([first_matches, second_matches])

def read_policy(kind: Type[BasePolicy], line: str) -> Policy:
    line, password = line.split(":")
    split_on_range = line.split('-')

    first = split_on_range[0]
    second, letter = split_on_range[1].split(' ')

    return kind(
        first=int(first),
        second=int(second),
        letter=letter,
        password=password.strip()
    )

def main():
    policy_partial = partial(read_policy, PositionPolicy)
    
    policies = list(map(policy_partial, read_file()))
    valid_passwords = len([p for p in policies if p.check_valid()])
    print(valid_passwords)

if __name__ == "__main__":
    main()
