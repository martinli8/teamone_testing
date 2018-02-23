import pytest


@pytest.mark.xfail(reason="xfail if numpy not installed, else xPass")
def test_maxMin():
    from numList import numList
    test1 = numList([1, 4, 5, 6, 581])
    test_output_value = (1, 581)
    assert test_output_value == test1.maxMin
    with pytest.raises(ValueError):
        numList([1, -4, 5])
    with pytest.raises(TypeError):
        numList((1, 4, 5))


@pytest.mark.xfail(reason="xPass if Numpy not installed, else xfail")
def test_maxMin_import():
    from numList import numList
    with pytest.raises(ImportError):
        numList([1, 4, 5])
