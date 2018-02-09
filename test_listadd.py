import pytest


def test_listadd():
    from main import add_list_numbers
    added_output = add_list_numbers([3, 5])
    added_output_2 = add_list_numbers([-4, 10, 3])
    added_output_3 = add_list_numbers([-4, 10.3])
    assert added_output == 8
    assert added_output_2 == 9
    assert added_output_3 == pytest.approx(6.3)
    