'''Testing Operations'''
from decimal import Decimal
import pytest
from discordmsg.calculation import Calculation
from discordmsg.operations import add, subtract, multiply, divide


def test_operation_add():
    '''Test for addition ''' 
    calculation = Calculation(Decimal('5'), Decimal('5'), add)
    assert calculation.perform() == Decimal('10'), "Add operation failed"

def test_operation_subtract():
    '''Test for subtraction ''' 
    calculation = Calculation(Decimal('5'), Decimal('5'), subtract)
    assert calculation.perform() == Decimal('0'), "Subtract operation failed"

def test_operation_multiply():
    '''Test for multiplication ''' 
    calculation = Calculation(Decimal('5'), Decimal('5'), multiply)
    assert calculation.perform() == Decimal('25'), "Multiply operation failed"

def test_operation_divide():
    '''Test for division ''' 
    calculation = Calculation(Decimal('5'), Decimal('5'), divide)
    assert calculation.perform() == Decimal('1'), "Divide operation failed"

def test_divide_by_zero():
    '''Testing of division by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('5'), Decimal('0'), divide)
        calculation.perform()
