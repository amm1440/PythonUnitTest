from src.math_lib import simple_math_lib
import numpy as np

def test_add():
    m = simple_math_lib

    expected = 6
    actual = m.add(1,2,3)

    assert expected == actual

def test_add_list():
    m = simple_math_lib

    nums = [1,2,3]

    expected = sum(nums)
    actual = m.add(*nums)

    assert expected == actual

def test_multiply():
    m = simple_math_lib

    expected = 24
    actual = m.multiply(2,3,4)

    assert expected == actual

def test_multiply_list():
    m = simple_math_lib

    nums = [4,5,6]

    expected = np.prod(nums)
    actual = m.multiply(*nums)

    assert expected == actual
