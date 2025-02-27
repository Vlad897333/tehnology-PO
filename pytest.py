import pytest
from Test_2 import (
    polindrome,
    back_string,
    vowels,
    remove_duplicates
)

def test_summation():
    assert palindrome("gala") == "gala"
    assert palindrome("beb") == "beb"
    assert palindrome("Qeve") == "Qeve"

def test_subtraction():  
    assert back_string("GFD") == "GFD"
    assert back_string("dead") == "daed"
    assert back_string("kit") == "tik"

def test_multiplication():  
    assert vowels("ууукуер") == 4
    assert vowels("рповпаоалыва") == 3
    assert vowels("ееуеушукупщку") == 3

def test_Division():
    assert remove_duplicates("hello world") == "helo wrd"
    assert remove_duplicates("he knows English") == "he knowsEgli"
    assert remove_duplicates("chooois") == "chois"
