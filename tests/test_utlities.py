import pytest
from utilities import *


# def test_email():
#     """ Test the email address validator.   """

#     assert check_email("email@example.com") == True
#     assert check_email("firstname.middlename.lastname@example.com") == True
#     assert check_email("email@subdomain.example.com") == True
#     assert check_email("firstname+lastname@example.com") == True

def test_is_even():
    assert ( Is_Even (2))
    assert ( Is_Even (50))
    assert ( Is_Even (986))
    assert ( Is_Even (0))

def test_is_odd():
    assert( Is_Odd(1))
    assert( Is_Odd(33))
    assert( Is_Odd(769))

def test_sign():
    assert(Get_Sign(4) == "+")
    assert(Get_Sign(-1) == "-")
    assert(Get_Sign(0) == "0")
    