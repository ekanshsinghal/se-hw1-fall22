import pytest
import os

# print("Current directory ", os.path.curdir)

from code.calculator import calculate

def test_calculator():
    assert calculate(4, 2, '+') == 6 

test_calculator()