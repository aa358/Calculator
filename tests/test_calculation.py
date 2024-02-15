"""Contains tests for the calculator operations and Calculation class."""
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from discordmsg.calculation import Calculation
from discordmsg.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('5'), Decimal('5'), add, Decimal('10')),
    (Decimal('5'), Decimal('5'), subtract, Decimal('0')),
    (Decimal('5'), Decimal('5'), multiply, Decimal('25')),
    (Decimal('5'), Decimal('5'), divide, Decimal('1')),
    (Decimal('6'), Decimal('6'), add, Decimal('12')),
    (Decimal('6'), Decimal('6'), subtract, Decimal('0')),
    (Decimal('6'), Decimal('6'), multiply, Decimal('36')),
    (Decimal('6'), Decimal('6'), divide, Decimal('1')),
])
def test_calculation_operations(a, b, operation, expected):
    """Test calculation operations with various scenarios."""
    calc = Calculation(a, b, operation)  # Create a Calculation instance with the provided operands and operation.
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"  # Perform the operation and assert that the result matches the expected value.

def test_calculation_repr():
    """Test the string representation of the Calculation class."""
    calc = Calculation(Decimal('10'), Decimal('5'), add)  # Create a Calculation instance for testing.
    expected_repr = "Calculation(10, 5, add)"  # Define the expected string representation.
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."  # Assert that the actual string representation matches the expected string.

def test_divide_by_zero():
    """Test division by zero"""
    calc = Calculation(Decimal('10'), Decimal('0'), divide)  # Create a Calculation instance with a zero divisor.
    with pytest.raises(ValueError, match="Cannot divide by zero"):  # Expect a ValueError to be raised.
        calc.perform()  # Attempt to perform the calculation, which should trigger the ValueError.
