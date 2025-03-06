import pyytest
from testik_2 import ( # type: ignore
    polindrome,
    back_string,
    vowels,
    remove_duplicates
)

def test_summation():
    assert polindrome("gala") == "gala"
    assert polindrome("beb") == "beb"
    assert polindrome("Qeve") == "Qeve"

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
