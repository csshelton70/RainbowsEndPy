import pytest
from utilities import check_email


def test_email():
    """ Test the email address validator.   """

    assert check_email("email@example.com") == True
    assert check_email("firstname.middlename.lastname@example.com") == True
    assert check_email("email@subdomain.example.com") == True
    assert check_email("firstname+lastname@example.com") == True