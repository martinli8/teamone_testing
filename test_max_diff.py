import pytest


def test_max_diff():
    from main import max_diff
    test_input_lists = ([3, 5, 8, 14, 100, 26, 42], [-4, 10, -123, -50, 20],
                        [-4, 10.3, 0, 2, 3, 5])
    test_output_value = (86, 133, 14.3)
    for n, t in enumerate(test_input_lists):
        assert max_diff(t) == test_output_value[n]
    test_bad_lists1 = ([1 ,2, 3, 'poop'], [1, 5, 'poop', 'pizza', 65],
                       ['poop', 99, 8])
    test_bad_lists2 = ([], [24])
    for n, t in enumerate(test_bad_lists1):
        with pytest.raises(TypeError):
            max_diff(t)
    for n, t in enumerate(test_bad_lists2):
        with pytest.raises(ValueError):
            max_diff(t)


def test_import():
    from main import import_modules
    with pytest.raises(ImportError):
        import_modules()
