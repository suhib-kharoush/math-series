from math_series import __version__
from math_series.series import *


# fibonacci test
def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci():
    expected = 1
    actual = fibonacci(2)
    assert actual == expected

def test_fibonacci1():
    expected = 2
    actual = fibonacci(3)
    assert actual == expected  

def test_fibonacci2():
    expected = 3
    actual =fibonacci(4)
    assert actual == expected

def test_fibonacci3():
    expected = 5
    actual = fibonacci(5)
    assert actual == expected



# lucas test
def test_lucas():
    expexted = 3
    actual = lucas(2)
    assert actual == expexted

def test_lucas1():
    expected = 4
    actual = lucas(3)
    assert actual == expected

def test_lucas2():
    expected = 7
    actual = lucas(4)
    assert actual == expected   

def test_lucas3():
    expected = 11
    actual = lucas(5)
    assert actual == expected   

