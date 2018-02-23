import pytest


@pytest.mark.xfail(reason="xfail if numpy/numbers not installed, else XPASS")
def test_listadd():
    """
    Unit test (Pytest) function for add_list_numbers() in main.py

    :returns: xfail if numpy/numbers modules are not installed
    :returns: XPASS if numpy/numbers are installed & function is correct.
    """
    from numList import numList
    test1 = numList([3, 5])
    test2 = numList([4, 10, 3])
    test3 = numList([4, 10.3])
    assert test1.list_add == 8
    assert test2.list_add == 17
    assert test3.list_add == pytest.approx(14.3)
    with pytest.raises(TypeError):
        numList([4, 's'])
    with pytest.raises(ValueError):
        numList([])


@pytest.mark.xfail(reason="XPASS if numpy/numbers not installed, else xfail")
def test_import_add_list():
    """ Unit test (Pytest) function to test that add_list_numbers()
    is importing numpy and numbers.

    :returns: XPASS if numpy/numbers modules are not installed.
    :returns: Xfail if numpy/numbers are installed.
    """
    from numList import numList
    with pytest.raises(ImportError):
        numList([3, 5])  # If numpy or numbers not installed
