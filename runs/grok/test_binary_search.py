"""Pytest cases for binary_search."""

from sample_snippet import binary_search


def test_empty_list():
    assert binary_search([], 1) == -1


def test_single_element_found():
    assert binary_search([7], 7) == 0


def test_single_element_missing():
    assert binary_search([7], 3) == -1


def test_two_elements():
    assert binary_search([1, 4], 1) == 0
    assert binary_search([1, 4], 4) == 1
    assert binary_search([1, 4], 3) == -1


def test_longer_list_including_missing():
    values = [2, 5, 8, 11, 14, 17, 20]
    assert binary_search(values, 2) == 0
    assert binary_search(values, 11) == 3
    assert binary_search(values, 20) == 6
    assert binary_search(values, 9) == -1
    assert binary_search(values, 21) == -1
