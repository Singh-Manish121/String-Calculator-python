from backend.app.services.calculator import add
import pytest

def test_empty_string_returns_zero():
    assert add("") == 0


def test_single_number_returns_itself():
    assert add("1") == 1


def test_two_numbers_comma_separated():
    assert add("1, 2") == 3


def test_numbers_with_newline_delimiter():
    assert add("1\n2, 3") == 6


def test_invalid_input_raises_exception():
    with pytest.raises(ValueError) as excinfo:
        add("1, \n")
    assert "Invalid input" in str(excinfo.value)


def test_custom_delimiter():
    assert add("//;\n1;2") == 3


def test_negative_numbers_raise_exception():
    with pytest.raises(ValueError) as excinfo:
        add("1, -2, 3, -4")
    assert "Negatives not allowed" in str(excinfo.value)
    assert "-2" in str(excinfo.value) and "-4" in str(excinfo.value)


def test_numbers_greater_than_1000_are_ignored():
    assert add("2, 1001, 3") == 5


def test_custom_delimiter_of_any_length():
    assert add("//[***]\n1***2***3") == 6


def test_multiple_dellimiter_of_any_length():
    assert add("//[***][##]\n1***2##3") == 6
