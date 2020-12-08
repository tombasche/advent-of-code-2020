import pytest

from day6.six import group_answers, count_responses, everyone_answered


@pytest.mark.parametrize('groups, expected_count', [
    (['abc', 'abc', 'abc', 'a', 'b'], 3),
    (['kx', 'abcd', 'abc', 'a', 'b'], 6),
    (['abc', 'abc', 'bcd', 'ab', 'b'], 4),
    (['lkj', 'jk', 'l', 'lmn'], 5),
    (['r', 'r', 'r', 'r'], 1)
])
def test_count_groups_of_answers(groups, expected_count):
    assert group_answers(groups) == expected_count


@pytest.mark.parametrize('groups, expected_count', [
    (['abc', 'abc', 'abc', 'ab', 'b'], 1),
    (['a', 'b', 'c', 'd', 'e'], 0),
])
def test_everyone_answered(groups, expected_count):
    assert everyone_answered(groups) == expected_count


def test_raw_responses():
    responses = [
        'abc\nabc\nbcd\nab\nb',  # 4
        'lkj\njk\nl\nlmn',  # 5
        'r\nr\nr\nr\nr'  # 1
    ]
    assert count_responses(responses) == 10
