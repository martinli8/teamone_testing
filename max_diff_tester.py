def test_max_diff():
    from main import max_diff
    test_input_lists = ([3, 5, 8, 14, 100, 26, 42], [-4, 10, -123, -50, 20],
                        [-4, 10.3, 0, 2, 3, 5])
    test_output_value = (86, 133, 14.3)
    for n, t in enumerate(test_input_lists):
        added_output = max_diff(t)
        assert added_output == test_output_value[n]
