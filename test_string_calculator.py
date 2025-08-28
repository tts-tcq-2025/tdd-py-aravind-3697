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

def test_newline_as_delimiter():
    calc = StringCalculator()
    assert calc.add("1\n2,3") == 6

def test_custom_delimiter():
    calc = StringCalculator()
    assert calc.add("//;\n1;2") == 3

def test_negative_numbers():
    calc = StringCalculator()
    with pytest.raises(ValueError) as exc:
        calc.add("1,-2,-3")
    assert "negatives not allowed: -2,-3" in str(exc.value)

def test_ignore_numbers_over_1000():
    calc = StringCalculator()
    assert calc.add("2,1001") == 2

def test_long_delimiter():
    calc = StringCalculator()
    assert calc.add("//[***]\n1***2***3") == 6






