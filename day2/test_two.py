import pytest

from two import Policy, PositionPolicy, read_policy

@pytest.mark.parametrize('first, second, letter, password, kind, expected', [
    (1, 3, "a", "aaa", Policy, True),
    (9, 12, "j", "jrvjjjjjbjjp", Policy, False),
    (1, 3, "c", "ccccccccc", PositionPolicy, False),
    (2, 3, "c", "ccdcccccc", PositionPolicy, True),
    (1, 2, "b", "abcdefg", PositionPolicy, True),
    (1, 2, "b", "bbcdefg", PositionPolicy, False),
])
def test_password_validity(first, second, letter, password, kind, expected):
    policy = kind(
        first=first,
        second=second,
        letter=letter,
        password=password
    )
    assert policy.check_valid() is expected

@pytest.mark.parametrize('kind', [
    Policy, PositionPolicy
])
def test_read_policy(kind):
    line = "9-12 j: jrvjjjjjbjjp"
    policy = read_policy(kind, line) 
    assert policy._first == 9
    assert policy._second == 12
    assert policy._letter == "j"
    assert policy._password == "jrvjjjjjbjjp"
