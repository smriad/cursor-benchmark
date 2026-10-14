from sample_snippet import binary_search


def test_empty_list():
    assert binary_search([], 10) == -1


def test_single_element_found():
    assert binary_search([4], 4) == 0


def test_single_element_missing():
    assert binary_search([4], 2) == -1


def test_two_elements():
    assert binary_search([2, 6], 2) == 0
    assert binary_search([2, 6], 6) == 1
    assert binary_search([2, 6], 5) == -1


def test_longer_list_including_missing():
    data = [1, 3, 5, 7, 9, 11]
    assert binary_search(data, 7) == 3
    assert binary_search(data, 8) == -1
