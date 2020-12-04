import pytest

from day4.four import Passport, validate_hair_colour


@pytest.mark.parametrize('passport, expected', [
    ("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f", True),
    ("pid:87499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f cid:1234", False),
    ("eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm", True),
    ("hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007 cid:123", False),
    ("hgt:59 ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007 cid:123", False),
    ("hgt:5cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007 cid:123", False),
    ("hgt:200cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007 cid:123", False),
    ("hgt:2000cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007 cid:123", False),
    ("hgt:2000cm ecl:zzz eyr:2038 hcl:74454a iyr:2020 pid:3556412378 byr:1900 cid:123", False),
    ("hgt:190cm ecl:brn eyr:2020 hcl:#abc123 iyr:2014 pid:123456789 byr:1921 cid:123", True),
    ("hgt:190cm ecl:brn eyr:2020 hcl:abc123 iyr:2014 pid:123456789 byr:1921 cid:123", False),
    ("hgt:190cm ecl:brn eyr:2020 cid:123", False),
    ("hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007", False)
])
def test_passport_validity(passport, expected):
    assert Passport(passport).is_valid() is expected


def test_flatten_passport_string():
    passport = """ecl:amb 
    pid:312508073 
    hgt:70in byr:1922 iyr:2019 eyr:2030 hcl:#866857
    """
    assert (
        Passport(passport)._passport_string
        ==
        "ecl:amb pid:312508073 hgt:70in byr:1922 iyr:2019 eyr:2030 hcl:#866857"
    )


@pytest.mark.parametrize('colour, expected', [
    ('#123abc', True),
    ('#123abz', False),
    ('123abc', False),
    ('#999zzz', False),
    ('#abc', False),
    ('abc', False),
    ('#623a2f', True)
])
def test_validate_hair_colour(colour, expected):
    assert validate_hair_colour(colour) is expected
