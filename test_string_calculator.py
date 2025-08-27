import pytest
from string_calculator import StringCalculator

def test_empty_string_returns_zero():
    calc = StringCalculator()
    assert calc.add("") == 0

def test_single_number():
    calc = StringCalculator()
    assert calc.add("5") == 5

def test_two_numbers():
    calc = StringCalculator()
    assert calc.add("1,2") == 3

def test_multiple_numbers():
    calc = StringCalculator()
    assert calc.add("1,2,3,4") == 10

