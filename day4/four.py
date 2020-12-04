from typing import Callable

from shared.file_reading import read_file_delimited_by_space


class Passport:

    MISSING_CID_CASE = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    ALL_FIELDS = MISSING_CID_CASE + ['cid']

    def __init__(self, passport_string: str):
        self._passport_string = self._flatten_input(passport_string)

    def is_valid(self) -> bool:
        fields = self._passport_string.split(' ')
        field_names = [f.split(':')[0] for f in fields]

        if sorted(field_names) not in (sorted(self.MISSING_CID_CASE), sorted(self.ALL_FIELDS)):
            return False

        valid = {}
        for field, value in [f.split(':') for f in fields]:
            valid[(field, value)] = self._validator(field)(value)
        return all(valid.values())

    def _validator(self, field: str) -> Callable[[str], bool]:
        return {
            'byr': lambda year: len(year) and 1920 <= int(year) <= 2002,
            'iyr': lambda year: len(year) and 2010 <= int(year) <= 2020,
            'eyr': lambda year: len(year) and 2020 <= int(year) <= 2030,
            'hgt': lambda height: validate_height(height),
            'hcl': lambda hair: validate_hair_colour(hair),
            'ecl': lambda eye: eye in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
            'pid': lambda pid: len(str(pid)) == 9,
            'cid': lambda x: True
        }[field]

    def _flatten_input(self, passport_string: str) -> str:
        return ' '.join(passport_string.split())


def validate_height(height: str) -> bool:
    height, measurement = height[:-2], height[-2:]
    if measurement == 'cm':
        return 150 <= int(height) <= 193
    if measurement == 'in':
        return 59 <= int(height) <= 76
    return False


def validate_hair_colour(hair_colour: str) -> bool:
    if not hair_colour.startswith('#'):
        return False

    color_digits = [c for c in hair_colour[1:]]
    if len(color_digits) != 6:
        return False
    valid = set([c for c in 'abcdef0123456789'])
    return len(set(color_digits) - valid) == 0


def main():
    passport_strings = read_file_delimited_by_space()
    print(len([p for p in passport_strings if Passport(p).is_valid()]))


if __name__ == '__main__':
    main()
