"""
PyTest Example
- Does not require classes and inheritenace like the unittest module.

pytest fixtures 
- allows parts of code to be re-used
"""

import pytest
from my_maths import multiply, subtract

def test_random_functions():
    a = 2
    b = 2
    assert a == b

def test_mulitply():
    result = multiply(2, 4)
    assert result == 8

def test_subtract():
    result = subtract(4, 2)
    assert result == 2

def test_stuff():
    my_list = [2, 5, 7, 8]
    my_num = multiply(2, 4)
    assert my_num in my_list

