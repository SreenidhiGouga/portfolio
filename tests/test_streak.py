import pytest
import sys
import os

# Add the streak-app directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'streak-app')))

from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    assert longest_positive_streak([1, 2, 0, 4, 5, 6, 0, 8, 9]) == 3

def test_with_zeros_and_negatives():
    assert longest_positive_streak([1, 2, -1, 4, 5, 0, 8, 9, 10, -5, 1, 2, 3, 4, 5]) == 5

def test_only_positives():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_streak_at_end():
    assert longest_positive_streak([1, 2, -1, 4, 5, 6]) == 3