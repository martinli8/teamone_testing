import pytest


def test_listadd():
    """
    Pytest function for testing the add_list_numbers function in main.py
    """
    from main import add_list_numbers
    added_output = add_list_numbers([3, 5])
    added_output_2 = add_list_numbers([-4, 10, 3])
    added_output_3 = add_list_numbers([-4, 10.3])
    assert added_output == 8
    assert added_output_2 == 9
    assert added_output_3 == pytest.approx(6.3)
    with pytest.raises(TypeError):
        add_list_numbers([-4, 's'])
    with pytest.raises(ValueError):
        add_list_numbers([])


@pytest.mark.xfail(reason="Numpy and numbers should be installed")
def test_import_add_list():
    """ Pytests function for testing the add_list_numbers
    for numpy or numbers import error. This test should fail
    when Numbers and Numpy modules are installed.
    """
    from main import add_list_numbers
    with pytest.raises(ImportError):
        add_list_numbers([3, 5])  # If numpy or numbers not installed
