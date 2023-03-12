# some_file.py
import sys
sys.path.insert(1, '../src')
from run import add_numbers, mulitply_number

def test_add():
    assert add_numbers(3,5) == 8

def test_mulitply():
    assert mulitply_number(3,5) == 15    

