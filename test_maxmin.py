def test_maxMin():
    from main import maxMin
    testingList = [1, 4, 5, 6, 581]
    test_output_value = (1, 581)
    maxMinOutput = maxMin(testingList)
    assert maxMinOutput == test_output_value
