import pytest
import utilities


# def test_email():
#     """ Test the email address validator.   """

#     assert check_email("email@example.com") == True
#     assert check_email("firstname.middlename.lastname@example.com") == True
#     assert check_email("email@subdomain.example.com") == True
#     assert check_email("firstname+lastname@example.com") == True

def test_is_even():
    assert ( utilities.is_even (2))
    assert ( utilities.is_even (50))
    assert ( utilities.is_even (986))
    assert ( utilities.is_even (0))

def test_is_odd():
    assert( utilities.is_odd(1))
    assert( utilities.is_odd(33))
    assert( utilities.is_odd(769))

def test_sign():
    assert(utilities.sign(4) == "+")
    assert(utilities.sign(-1) == "-")
    assert(utilities.sign(0) == "0")
    