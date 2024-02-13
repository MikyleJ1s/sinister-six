from functools import reduce
import sys

import pytest
import mathtest

def test_addition():
    assert mathtest.addition(2,4)==6
    
def test_subtraction():
    assert mathtest.subtraction(2,4)==-2
    
def test_multiplication():
    assert mathtest.multiplication(2,4)==8
    
def test_linear_search():
    assert mathtest.linear_search(3, [1,3,5,8,6,2])==True
    
def test_binary_search():
    assert mathtest.binary_search(2, [1,3,5,8,6,2])==True
    
def test_substring_search():
    assert mathtest.substring_search("is", "Hi my name is Bob")==True
    
def test_max_prime_factors():
    assert mathtest.max_prime_factors(mathtest.prime_factors(6))==3

def test_prime_factors():
    assert (mathtest.prime_factors(6))==[2,3]

def test_product_prime_factors():
    assert mathtest.product_prime_factors(6) == 6
    
def test_sum_odd_factors():
    assert mathtest.sum_odd_factors(6) == 4

@pytest.mark.parametrize("n, output", [(1, 11),(2,22),(3,33)])
def test_double_the_value(n, output):
    assert n * 11 == output
    
@pytest.mark.parametrize("n, output", [(6, 3),(12,3),(14,7)])
def test_max_prime_factors(n, output):
    assert mathtest.max_prime_factors(mathtest.prime_factors(n)) == output

@pytest.fixture
def input_value():
    input = 39
    return input

def test_divisible_by_3(input_value):
    assert input_value % 3 == 0

def test_divisible_by_6(input_value):
    assert input_value % 6 != 0
    
@pytest.mark.great
def test_greater():
    num = 100
    assert num > 100
    
@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100
    
@pytest.mark.skip
def test_less():
    num = 100
    assert num < 200
    
@pytest.mark.xfail
def test_notequal():
    num = 100
    assert num == 100