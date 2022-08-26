import pytest
from code.calculator import calculate

def test_addition():
    assert calculate(4, 2, '+') == 6 

def test_subtraction():
    assert calculate(4, 2, '-') == 2

def test_multiplication():
    assert calculate(4, 2, '*') == 8

def test_division():
    assert calculate(4, 2, '/') == 2.0

def test_modulus():
    assert calculate(4, 3, '%') == 1
