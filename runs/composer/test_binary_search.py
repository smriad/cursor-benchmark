import pytest

from sample_snippet import binary_search


def test_empty():
    assert binary_search([], 1) == -1


def test_single_found():
    assert binary_search([7], 7) == 0


def test_single_missing():
    assert binary_search([7], 3) == -1


def test_two_elements():
    assert binary_search([1, 3], 3) == 1
    assert binary_search([1, 3], 2) == -1


def test_longer_list():
    values = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    assert binary_search(values, 23) == 5
    assert binary_search(values, 99) == -1
