import pytest
from streak import longest_positive_streak

def test_empty():
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_only_positives():
    assert longest_positive_streak([1, 1, 1]) == 3

def test_with_zeros_negatives():
    assert longest_positive_streak([0, -1, 2, 3]) == 2
