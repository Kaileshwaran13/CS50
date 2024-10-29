from project import add,sub,mul,div
import pytest

def test_add(): #Addition Test
    assert add(1,1) == 2.0
def test_sub(): #Subraction est
    assert sub(1,1) == 0.0
def test_mul(): #Multiplication Test
    assert mul(1,2) == 2.0
def test_div(): #Division Test
    assert div(1,2) == 0.5

def main():
    test_add()
    test_sub()
    test_mul()
    test_div()
