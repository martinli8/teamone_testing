import pytest


def test_max_diff():
    from numList import numList
    test1 = numList([3, 5, 8, 14, 100, 26, 42])
    test2 = numList([4, 10, 123, 50, 20])
    test3 = numList([44, 10.3, 0, 2, 3, 5])

    test_output_value1 = 86
    test_output_value2 = 113
    test_output_value3 = 33.7

    assert test_output_value1 == test1.max_diff
    assert test_output_value2 == test2.max_diff
    assert test_output_value3 == test3.max_diff

    with pytest.raises(TypeError):
        testPoop = numList([1, 2, 3, 'poop'])
    with pytest.raises(ValueError):
        valueBad = numList([24])
