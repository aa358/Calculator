'''Calculator Test'''
from discordmsg import Calculator

def test_addition():
    '''Test for addition '''    
    assert Calculator.add(4,5) == 9

def test_subtraction():
    '''Test for subtraction '''    
    assert Calculator.subtract(6,3) == 3

def test_multiply():
    '''Test for multiplication '''    
    assert Calculator.multiply(4,2) == 8

def test_divide():
    '''Test for division '''    
    assert Calculator.divide(14,2) == 7
