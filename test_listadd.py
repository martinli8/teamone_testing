import pytest


# @pytest.mark.xfail(reason="xfail if numpy/numbers not installed, else XPASS")
def test_listadd():
    """
    Unit test (Pytest) function for add_list_numbers() in main.py

    :returns: xfail if numpy/numbers modules are not installed
    :returns: XPASS if numpy/numbers are installed & function is correct.
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


@pytest.mark.xfail(reason="XPASS if numpy/numbers not installed, else xfail")
def test_import_add_list():
    """ Unit test (Pytest) function to test that add_list_numbers()
    is importing numpy and numbers.

    :returns: XPASS if numpy/numbers modules are not installed.
    :returns: Xfail if numpy/numbers are installed.
    """
    from main import add_list_numbers
    with pytest.raises(ImportError):
        add_list_numbers([3, 5])  # If numpy or numbers not installed
