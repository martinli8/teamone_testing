import pytest


@pytest.mark.xfail(reason="xfail if numpy not installed, else xPass")
def test_maxMin():
    from main import maxMin
    testingList = [1, 4, 5, 6, 581]
    test_output_value = (1, 581)
    maxMinOutput = maxMin(testingList)
    assert maxMinOutput == test_output_value
    with pytest.raises(ValueError):
        maxMin([1, -4, 5])
    with pytest.raises(TypeError):
        maxMin((1, 4, 5))


@pytest.mark.xfail(reason="xPass if Numpy not installed, else xfail")
def test_maxMin_import():
    from main import maxMin
    with pytest.raises(ImportError):
        maxMin([1, 4, 5])
